
DC_CENSUS_TRACTS = 'http://opendata.dc.gov/datasets/6969dd63c5cb4d6aa32f15effb8311f3_8.zip'
DC_CENSUS_BLOCKS = 'http://opendata.dc.gov/datasets/c143846b7bf4438c954c5bb28e5d1a21_2.zip'

DC_GEOJSON_TRACTS = 'mapper/static/geojson/dc_census_tracts.geojson'
DC_GEOJSON_BLOCKS = 'mapper/static/geojson/dc_census_blocks.geojson'

GEO_LEVEL_CHOICES = [('tracts', 'Census Tracts'), ('blocks', 'Census Blocks')]

MATCH_KEY_CHOICES = [('geoid', 'GEO ID'),
                     ('tract', 'CENSUS TRACT'),
                     ('blkgrp', 'CENSUS BLOCK GROUP')]

COLUMNS_TO_AVOID = ['OBJECTID', 'TRACT', 'BLKGRP', 'GEOID']
