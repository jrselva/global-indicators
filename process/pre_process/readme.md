## Pre-processing
The files in this folder provide a workflow for extraction of study region specific resources to a series of geopackages for use in the main built environment analyses found in the 'process' folder.
Project, study region and resource parameters are defined using the following configuration files:

- configuration/config.yml (project configuration)
- configuration/regions.yml (city configuration)
- configuration/osm_open_space.yml (parameters for analysing areas of open space derived from OpenStreetMap)
- configuration/osm_destination_definitions.csv (terms used to identify destinations derived from OpenStreetMap)

A shell script can be used to execute the study region specific python scripts (prefixed `00` through `11`) to derive spatial data including walkable street network, destinations, population data, and hexagon grids into a standard shared format, before running the GTFS analysis for all cities with available data which have been configured for analysis. The shell script wrapper is run using `"bash ./process_region.sh"` followed by a list of study region names. The pre-processing procedure creates the geopackage and graphml files that are required as inputs for the main global indicators built environment analyses.

# set up spatial database container, based on PostgreSQL with PostGIS and pgRouting
Retrieve the docker image
```
docker pull pgrouting/pgrouting
```

Run the postgis server container with persistent storage (replace the password for Postgis to correspond to your project configuration)
```
docker run --name=postgis -d -e POSTGRES_PASSWORD=ghscic -p 127.0.0.1:5433:5432 --restart=unless-stopped --volume=/var/lib/postgis:/postgresql/13/main pgrouting/pgrouting
```

# run analysis environment
On linux:
```
docker run --rm -it --shm-size=2g --net=host -v "$PWD":/home/ghsci/work globalhealthyliveablecities/global-indicators /bin/bash
```
Or windows
```
docker run --rm -it --name=global-indicators --shm-size=2g --net=host -v "%cd%":/home/ghsci/work globalhealthyliveablecities/global-indicators /bin/bash
```

**Run pre-processing scripts:** `bash ./process_region.sh [city name] [city name] [city name] [...]`

**Pre-processing script details**

The study region specific scripts are run as follows, with output to "./data/study_regions/[city]_[region]_[year]/".
	-    `python 00_create_database.py $i`
	-    `python 01_create_study_region.py $i`
	-    `python 02_create_osm_resources.py $i`
	-    `python 03_create_network_resources.py $i`
	-    `python 04_create_hex_grid.py $i`
	-    `python 05_create_population_grid.py $i`
	-    `python 06_compile_destinations.py $i`
	-    `python 07_open_space_areas_setup.py $i`
	-    `python 08_locate_origins_destinations.py $i`
	-    `python 09_hex_destination_summary.py $i`
	-    `python 10_osm_audit_pop.py $i`
	-    `python 11_urban_covariates.py $i`
	-    `python _export_gpkg.py $i`

The final script is processed for all cities with available and configured GTFS data located in the process/data/GTFS folder,
    -   `python 12_all_cities_gtfs_analysis.py`

A summary of the GTFS headway analysis is output to `../data/GTFS/all_cities_comparison_{today}.csv`, and a geopackage of public transport stop locations with associated average daytime weekday headways:
`../data/GTFS/gtfs_frequent_transit_headway_{today}_python.gpkg`

The GTFS analysis is detailed in the file [./12_all_cities_gtfs_analysis_readme.md](./12_all_cities_gtfs_analysis_readme.md).
