"""
Locate origins destinations.

Calculate and store the distances to the two nearest nodes (node pairs)
on edges for all sample point origins Calculate and store the nearest
node (D-nodes) and euclidean distance to this for each destination.
"""

import time

import psycopg2
from _project_setup import *
from script_running_log import script_running_log
from sqlalchemy import create_engine, inspect


def main():
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = "Pre-prepare distance associations between origins, destinations and nearest node locations"
    sql_queries = {
        "Create sampling points along network at a regular interval": f"""
        DROP TABLE IF EXISTS {points};
        CREATE TABLE IF NOT EXISTS {points} AS
        WITH line AS
                (SELECT
                    ogc_fid,
                    (ST_Dump(ST_Transform(geom,{srid}))).geom AS geom
                FROM edges),
            linemeasure AS
                (SELECT
                    ogc_fid,
                    ST_AddMeasure(line.geom, 0, ST_Length(line.geom)) AS linem,
                    generate_series(0, ST_Length(line.geom)::int, {point_sampling_interval}) AS metres
                FROM line),
            geometries AS (
                SELECT
                    ogc_fid,
                    metres,
                    (ST_Dump(ST_GeometryN(ST_LocateAlong(linem, metres), 1))).geom AS geom
                FROM linemeasure)
        SELECT
            row_number() OVER() AS point_id,
            ogc_fid,
            metres,
            ST_SetSRID(ST_MakePoint(ST_X(geom), ST_Y(geom)), {srid}) AS geom
        FROM geometries;
        CREATE UNIQUE INDEX IF NOT EXISTS {points}_idx ON {points} (point_id);
        CREATE INDEX IF NOT EXISTS {points}_geom_idx ON {points} USING GIST (geom);
        """,
        "Delete any sampling points which were created within the bounds of areas of open space (ie. along paths through parks)...": f"""
        DELETE FROM {points} p
        USING open_space_areas o
        WHERE ST_Intersects(o.geom,p.geom);
        """,
        "Delete any sampling points intersecting grids with population estimated below minimum threshold...": f"""
        DELETE FROM {points} p
        USING {population_grid} o
        WHERE ST_Intersects(o.geom,p.geom)
        AND o.pop_est < {population['pop_min_threshold']};
        """,
        "Create new columns and indices for sampling point edge and node relations": """
        -- Split query in two parts to avoid memory errors
        -- Both parts of full query took just over 30 seconds for Bangkok (1472479 sampling points
        -- part 1
        DROP TABLE IF EXISTS sampling_locate_line;
        CREATE TABLE sampling_locate_line AS
        SELECT  s.point_id,
                    s.ogc_fid edge_ogc_fid,
                    s.metres,
                    "from" n1,
                    "to" n2,
                    e.geom AS edge_geom,
                    ST_LineLocatePoint(e.geom, n1.geom) llp1,
                    ST_LineLocatePoint(e.geom, s.geom) llpm,
                    ST_LineLocatePoint(e.geom, n2.geom) llp2,
                    s.geom
            FROM sampling_points_30m s
            LEFT JOIN edges e  ON s.ogc_fid = e.ogc_fid
            LEFT JOIN nodes n1 ON e."from" = n1.osmid
            LEFT JOIN nodes n2 ON e."to" = n2.osmid;

        -- part 2 (split to save memory on parallel worker query)
        DROP TABLE IF EXISTS sampling_temp;
        CREATE TABLE sampling_temp AS
        SELECT point_id,
               edge_ogc_fid,
               metres,
               n1,
               n2,
               ST_Length(ST_LineSubstring(t.edge_geom, LEAST(t.llp1,t.llpm),GREATEST(t.llp1,t.llpm)))::int n1_distance,
               ST_Length(ST_LineSubstring(t.edge_geom, LEAST(t.llp2,t.llpm),GREATEST(t.llp2,t.llpm)))::int n2_distance,
               t.geom
        FROM sampling_locate_line t;
        DROP TABLE sampling_points_30m;
        DROP TABLE sampling_locate_line;
        ALTER TABLE sampling_temp RENAME TO sampling_points_30m;
        CREATE UNIQUE INDEX IF NOT EXISTS sampling_points_30m_ix ON sampling_points_30m (point_id);
        CREATE INDEX IF NOT EXISTS sampling_points_30m_edge_ogc_fid_idx ON sampling_points_30m (edge_ogc_fid);
        CREATE INDEX IF NOT EXISTS sampling_points_30m_n1_idx ON sampling_points_30m (n1);
        CREATE INDEX IF NOT EXISTS sampling_points_30m_n2_idx ON sampling_points_30m (n2);
        CREATE INDEX IF NOT EXISTS sampling_points_30m_gix ON sampling_points_30m USING GIST (geom);
        """,
        "Record closest node and distance for destination points": """
        -- took 2 seconds to run for Bangkok (10,047 destinations)
        DROP TABLE IF EXISTS destinations_updated;
        CREATE TABLE IF NOT EXISTS destinations_updated AS
        SELECT  o.dest_oid,
                o.osm_id,
                o.dest_name,
                o.dest_name_full,
                o.edge_ogc_fid,
                o.n1,
                o.n2,
                -- to determine length along a line, the origin must be located the lower proportion along the line,
                -- hence the least and greatest queries
                ST_Length(ST_LineSubstring(o.edge_geom, LEAST(llp1,llpm),GREATEST(llp1,llpm)))::int n1_distance,
                ST_Length(ST_LineSubstring(o.edge_geom, LEAST(llp2,llpm),GREATEST(llp2,llpm)))::int n2_distance,
                ST_Distance(geom,match_point_geom)::int match_point_distance,
                o.match_point_geom,
                o.geom
        FROM
        (SELECT t.dest_oid,
                t.osm_id,
                t.dest_name,
                t.dest_name_full,
                t.geom,
                t.edge_ogc_fid,
                t.match_point_geom,
                t.n1,
                t.n2,
                t.edge_geom,
                ST_LineLocatePoint(t.edge_geom, n1.geom) llp1,
                ST_LineLocatePoint(t.edge_geom, t.match_point_geom) llpm,
                ST_LineLocatePoint(t.edge_geom, n2.geom) llp2
        FROM
        (SELECT d.dest_oid,
                d.osm_id,
                d.dest_name,
                d.dest_name_full,
                d.geom,
                e.geom edge_geom,
                e.edge_ogc_fid,
                ST_ClosestPoint(e.geom,d.geom) AS match_point_geom,
                e.n1,
                e.n2
        FROM destinations d
        CROSS JOIN LATERAL (
            SELECT e.ogc_fid edge_ogc_fid,
                   e."from" n1,
                   e."to" n2,
                   e.geom
            FROM edges e
            ORDER BY e.geom <-> d.geom
            LIMIT 1
        ) e
        ) t
        LEFT JOIN nodes n1 ON t.n1 = n1.osmid
        LEFT JOIN nodes n2 ON t.n2 = n2.osmid
        ) o;
        DROP TABLE destinations;
        ALTER TABLE destinations_updated RENAME TO destinations;
        CREATE UNIQUE INDEX IF NOT EXISTS destinations_ix ON destinations (dest_oid);
        CREATE INDEX IF NOT EXISTS destinations_edge_ogc_fid_idx ON destinations (edge_ogc_fid);
        CREATE INDEX IF NOT EXISTS destinations_n1_idx ON destinations (n1);
        CREATE INDEX IF NOT EXISTS destinations_n2_idx ON destinations (n2);
        CREATE INDEX IF NOT EXISTS destinations_gix ON destinations USING GIST (geom);
        """,
        "Recreate urban sample points": """
           DROP TABLE IF EXISTS urban_sample_points;
           CREATE TABLE IF NOT EXISTS urban_sample_points AS
           SELECT a.*
           FROM sampling_points_30m a,
                urban_study_region b
           WHERE ST_Intersects(a.geom,b.geom);
           CREATE UNIQUE INDEX IF NOT EXISTS urban_sample_points_ix ON urban_sample_points (point_id);
           CREATE INDEX IF NOT EXISTS urban_sample_points_gix ON urban_sample_points USING GIST (geom);
        """,
    }

    conn = psycopg2.connect(database=db, user=db_user, password=db_pwd)
    curs = conn.cursor()
    for q in sql_queries:
        print(f"\n{q}... ")
        start_time = time.time()
        curs.execute(sql_queries[q])
        conn.commit()
        end_time = time.time()
        print(f"Completed in {(end_time - start_time) / 60:.02f} minutes.")

    script_running_log(script, task, start, locale)
    conn.close()


if __name__ == "__main__":
    main()
