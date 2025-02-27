"""
GTFS configuration.

This script contain GTFS parameters defined for each study regions for
importing to conduct stop frequency analysis.

Note: most cities' parameters are based upon the stardard GTFS format
however, this may not be the case for every study regions
therefore, further research may be needed to define correct agency and route types.
"""

# set up study region GTFS config
analysis_period = ["07:00:00", "19:00:00"]
headway_intervals = [20, 30]  # not implemented
dissolve_cities = [
    "hanoi"
]  # aggregate mean of headways by stop_id; does not retain mode
GTFS = {
    "maiduguri": [],
    "hong_kong": [
        {
            "gtfs_filename": "gtfs_china_hongkong/gtfs_china_hongkong_hk_2019",
            "gtfs_provider": "data.gov.hk",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                113.9100000193474,
                22.224267038676757,
                114.28820272994885,
                22.566461572803423,
            ),
            "crs": "epsg:32650",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "chennai": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_india_chennai/metropolitan-transport-corporation_20101218_1110",
            "gtfs_provider": "Metropolitan Transport Corporation (via GTFS Exchange)",
            "gtfs_year": "2010",
            "start_date_mmdd": "20100405",
            "end_date_mmdd": "20100605",
            "bbox": (
                80.13557688345986,
                12.84745650235429,
                80.3375087202582,
                13.239675620841895,
            ),
            "crs": "epsg:32644",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_india_chennai/chennai-rail-gtfs-master/fixtures",
            "gtfs_provider": "https://github.com/justjkk/chennai-rail-gtfs",  # data generated in 2011, only intended as roughly indicative (better than nothing)
            "gtfs_year": "2016",  # note - has notional coverage from 2011 to 2020; so 2016 and 2019 are no different in data
            "start_date_mmdd": "20161008",
            "end_date_mmdd": "20161205",
            "bbox": (
                80.13557688345986,
                12.84745650235429,
                80.3375087202582,
                13.239675620841895,
            ),
            "crs": "epsg:32644",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
    ],
    "bangkok": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_thailand_bangkok/gtfs_thailand_bangkok_2021",
            "gtfs_provider": "https://namtang.otp.go.th/",
            "gtfs_year": "2021",
            "start_date_mmdd": "20210405",
            "end_date_mmdd": "20210605",
            "bbox": (
                100.3141282074272027,
                13.5717929649253772,
                100.9072403990231379,
                13.9696568160725310,
            ),
            "crs": "epsg:32647",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "hanoi": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_vietnam_hanoi/hanoi_gtfs_am",  # ~6:30 to 10:30
            "gtfs_provider": "World Bank",
            "gtfs_year": "2018",
            "start_date_mmdd": "20180405",
            "end_date_mmdd": "20180605",
            "bbox": (
                105.34078402749672,
                20.595670595639348,
                106.02487857831515,
                21.305560533209803,
            ),
            "crs": "epsg:32648",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },  # The idea might be, post hoc the headways for each stop (am, md, pm) are averaged
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_vietnam_hanoi/hanoi_gtfs_md",  # ~10:30 to 17:30
            "gtfs_provider": "World Bank",
            "gtfs_year": "2018",
            "start_date_mmdd": "20180405",
            "end_date_mmdd": "20180605",
            "bbox": (
                105.34078402749672,
                20.595670595639348,
                106.02487857831515,
                21.305560533209803,
            ),
            "crs": "epsg:32648",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_vietnam_hanoi/hanoi_gtfs_pm",  # ~16:30 to 20:30
            "gtfs_provider": "World Bank",
            "gtfs_year": "2018",
            "start_date_mmdd": "20180405",
            "end_date_mmdd": "20180605",
            "bbox": (
                105.34078402749672,
                20.595670595639348,
                106.02487857831515,
                21.305560533209803,
            ),
            "crs": "epsg:32648",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
    ],
    "graz": [],
    "ghent": [],
    "bern": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_swiss_bern/gtfs_swiss_bern_SCF_20181209",
            "gtfs_provider": "opentransportdata.swiss",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                7.35925731707479,
                46.9198803454112,
                7.502082155046318,
                46.99460688285978,
            ),
            "crs": "epsg:32633",
            "validation": False,
            "modes": {
                # manually identified Swiss route types using route description
                # see 'Switzerland GTFS lookup.csv'
                #  https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [900], "agency_id": None},
                "Metro": {"route_types": [100, 400, 401], "agency_id": None},
                "Rail": {
                    "route_types": [102, 103, 106, 1700],
                    "agency_id": None,
                },
                "Bus": {"route_types": [700], "agency_id": None},
                "Ferry": {"route_types": [1000], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [1300], "agency_id": None},
                "Funicular": {"route_types": [1400], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "olomouc": [],
    "odense": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_denmark_odense/gtfs_denmark_odense_Rejseplanen_20190314",
            "gtfs_provider": "https://www.rejseplanen.dk/ (via OpenMobilityData)",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                10.30381254797572,
                55.33877682649117,
                10.46065004137351,
                55.44769823364561,
            ),
            "crs": "epsg:32632",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "vic": [],
    "belfast": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_uk_belfast/data nicva org/metrogtfs",
            "gtfs_provider": "Translink (via ODI Belfast / OpenDataNI)",
            "gtfs_year": "2017",
            "start_date_mmdd": "20170405",
            "end_date_mmdd": "20170605",
            "bbox": (
                -6.069370813429552,
                54.53841202212822,
                -5.808356706713072,
                54.66949357865659,
            ),
            "crs": "epsg:29902",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "adelaide": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_au_adelaide/gtfs_au_sa_adelaidemetro_20191004",
            "gtfs_provider": "AdelaideMetro",
            "gtfs_year": "2019",
            # define month and day for "representative period" start and end date ie. not in school time
            "start_date_mmdd": "20191008",
            "end_date_mmdd": "20191205",
            # get bounding box from study region boundary shapefile
            # bounding box formatted as a 4 element tuple: (lng_max, lat_min, lng_min, lat_max)
            # you can generate a bounding box by going to http://boundingbox.klokantech.com/ and selecting the CSV format.
            "bbox": (
                138.46098938116273,
                -35.15966609024628,
                138.7483172991119,
                -34.71454282915053,
            ),
            "crs": "epsg:7845",
            # define modes for GTFS feed(s) as per agency_id codes in agency.txt below
            # this may varied across different cities
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "melbourne": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_au_melbourne/gtfs_au_vic_ptv_20191004",
            "gtfs_provider": "PublicTransportVictoria",
            "gtfs_year": "2019",
            "start_date_mmdd": "20191008",
            "end_date_mmdd": "20191205",
            "bbox": (
                144.5906504679234,
                -38.21131973169178,
                145.39850460739467,
                -37.61837232908795,
            ),
            "crs": "epsg:7845",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                # Note that additional restriction by agency as per http://data.ptv.vic.gov.au/downloads/PTVGTFSReleaseNotes.pdf
                # would introduce bias against Melbourne relative to other cities
                # which would not be subject to such exclusions (ie. exlcuding regional services)
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "sydney": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_au_sydney/gtfs_au_nsw_tfnsw_complete_20190619",
            "gtfs_provider": "NSW",
            "gtfs_year": "2019",
            "start_date_mmdd": "20191008",
            "end_date_mmdd": "20191205",
            "bbox": (
                150.62904566865876,
                -34.12321411958463,
                151.3206967438455,
                -33.66275213092711,
            ),
            "crs": "epsg:7845",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                # with modifications based on routes.txt route descriptions (contra standard)
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [401], "agency_id": None},
                "Rail": {"route_types": [401], "agency_id": None},
                "Bus": {"route_types": [700, 712, 714], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "phoenix": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_us_phoenix/gtfs_us_phoenix_valleymetro_190403",
            "gtfs_provider": "Valleymetro",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -112.32944601938362,
                33.286173152579444,
                -111.92001601610974,
                33.715160472950544,
            ),
            "crs": "epsg:32612",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "mexico_city": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_mexico_mexico_city/gtfs_mexico_mexico_city_fdg_20180101",
            "gtfs_provider": "FederalDistrictGovernment",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -99.38398744740229,
                19.01447489845741,
                -98.76238427264913,
                19.875453171171706,
            ),
            "crs": "epsg:32614",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "baltimore": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_us_baltimore/gtfs_us_baltimore_MarylandMTA_20180101",
            "gtfs_provider": "MarylandMTA",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -76.84177077970973,
                39.108360751446845,
                -76.3976914329063,
                39.50954447281339,
            ),
            "crs": "epsg:32618",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "sao_paulo": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_brazil_sao_paulo/gtfs_brazil_sao_paulo_SPTrans_20080101",
            "gtfs_provider": "SPTrans",
            "gtfs_year": "2019",
            "start_date_mmdd": "20191008",
            "end_date_mmdd": "20191205",
            "bbox": (
                -46.830230353747325,
                -23.819961957892033,
                -46.36030177462541,
                -23.392833498544647,
            ),
            "crs": "epsg:32723",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "auckland": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_newzealand_auckland/gtfs_newzealand_auckland_AucklandTransport_20190928",
            "gtfs_provider": "AucklandTransport",
            "gtfs_year": "2019",
            "start_date_mmdd": "20191008",
            "end_date_mmdd": "20191205",
            "bbox": (
                174.57726564925753,
                -37.089137447205424,
                174.98796590474112,
                -36.68399669533542,
            ),
            "crs": "epsg:2193",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "seattle": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_us_seattle/gtfs_us_seattle_kingcountymetro_20190319",
            "gtfs_provider": "KingCountyMetro",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -122.64010687230011,
                47.053580596564274,
                -122.01322166312818,
                48.01908489809623,
            ),
            "crs": "epsg:32610",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "cologne": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_germany_cologne/gtfs_germany_cologne_VR_20171210",
            "gtfs_provider": "VRS",
            "gtfs_year": "2018",
            "start_date_mmdd": "20180405",
            "end_date_mmdd": "20180605",
            "bbox": (
                6.809029241944378,
                50.827121084583915,
                7.150063369469329,
                51.0743422371189,
            ),
            "crs": "epsg:32631",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        }
    ],
    "barcelona": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_spain_barcelona/gtfs_spain_barcelona_AMB_20190404",
            "gtfs_provider": "AMB",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                1.9362482062659465,
                41.259035278051186,
                2.3025592806940103,
                41.53879596970758,
            ),
            "crs": "epsg:25831",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_spain_barcelona/gtfs_spain_barcelona_TMB_20190402",
            "gtfs_provider": "TMB",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                1.9362482062659465,
                41.259035278051186,
                2.3025592806940103,
                41.53879596970758,
            ),
            "crs": "epsg:25831",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_spain_barcelona/gtfs_spain_barcelona_Trambaix_20190303",
            "gtfs_provider": "TMB",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                1.9362482062659465,
                41.259035278051186,
                2.3025592806940103,
                41.53879596970758,
            ),
            "crs": "epsg:25831",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
    ],
    "valencia": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_spain_valencia/gtfs_spain_valencia_MetroValencia_20190403",
            "gtfs_provider": "metroValencia",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -0.4382381213256684,
                39.36674924068613,
                -0.287357243393633,
                39.570614328215,
            ),
            "crs": "epsg:25830",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_spain_valencia/gtfs_spain_valencia_EMT_20190403",
            "gtfs_provider": "EMT",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -0.4382381213256684,
                39.36674924068613,
                -0.287357243393633,
                39.570614328215,
            ),
            "crs": "epsg:25830",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
    ],
    "lisbon": [
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/carris/gtfs_portugal_lisbon_carris_20111015",
            "gtfs_provider": "carris",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/metro-de-lisboa/gtfs_portugal_lisbon_metro-de-lisboa_20111015",
            "gtfs_provider": "metro-de-lisboa",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/Fertagus/gtfs_portugal_lisbon_Fertagus_20111015",
            "gtfs_provider": "Fertagus",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/MTS/gtfs_portugal_lisbon_MTS_20150105",
            "gtfs_provider": "MTS",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/Soflusa/gtfs_portugal_lisbon_Soflusa_20111015",
            "gtfs_provider": "Soflusa",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/transtejo/gtfs_portugal_lisbon_transtejo_20111015",
            "gtfs_provider": "transtejo",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
        {
            "gtfs_filename": "GTFS/gtfs_input_data/gtfs_portugal_lisbon/CP/gtfs_portugal_lisbon_CP_20111015",
            "gtfs_provider": "CP",
            "gtfs_year": "2019",
            "start_date_mmdd": "20190405",
            "end_date_mmdd": "20190605",
            "bbox": (
                -9.235578212347956,
                38.68690034668498,
                -9.084818912087886,
                38.80035575382607,
            ),
            "crs": "epsg:3763",
            "validation": False,
            "modes": {
                # as per https://developers.google.com/transit/gtfs/reference#routestxt
                "Tram": {"route_types": [0], "agency_id": None},
                "Metro": {"route_types": [1], "agency_id": None},
                "Rail": {"route_types": [2], "agency_id": None},
                "Bus": {"route_types": [3], "agency_id": None},
                "Ferry": {"route_types": [4], "agency_id": None},
                "Cable tram": {"route_types": [5], "agency_id": None},
                "Aerial lift": {"route_types": [6], "agency_id": None},
                "Funicular": {"route_types": [7], "agency_id": None},
                "Trolleybus": {"route_types": [11], "agency_id": None},
                "Monorail": {"route_types": [12], "agency_id": None},
            },
        },
    ],
}
