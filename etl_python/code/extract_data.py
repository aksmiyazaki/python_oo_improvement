from os import chdir
chdir('/home/aksmiyazaki/git/python_oo_improvement/etl_python/code')


import argparse
from os import listdir
from os.path import join
from os import getcwd
import geoparse

args = None
input_dir = None

parser = argparse.ArgumentParser(description='Read raw data files and parse its contents')
parser.add_argument('--ip', type=str, nargs='+', help='Input path of the raw_data files.')
args = parser.parse_args()

if args == None:
    input_dir = '/home/aksmiyazaki/git/python_oo_improvement/etl_python/raw_data'

data_list = listdir(input_dir)
geo_point = None
geo_parser = geoparse.GeoParser()

def next_state(cur_state):
    """Given a state, returns the next expected state.
    It is used to control the kind of state machine that was implemented reading files.
    Keyword arguments:
    cur_state -- the current state of the file reader
    """
    if cur_state == geoparse.RowDataType.SEEK_LAT:
        return geoparse.RowDataType.SEEK_LON
    elif cur_state == geoparse.RowDataType.SEEK_LON:
        return geoparse.RowDataType.SEEK_DIST
    elif cur_state == geoparse.RowDataType.SEEK_DIST:
        return geoparse.RowDataType.SEEK_LAT
    else:
        raise Exception(f"[ERROR]   There is no next state for current {cur_state}")

def reset_state(parser):
    """
    Resets the state of the file reader.
    Keyword arguments:
    parser -- a GeoParser object to be reseted
    """
    parser.reset()
    return parser, geoparse.RowDataType.SEEK_LAT

# This is data extraction's the main loop
for raw_file in data_list:
    raw_file = data_list[0]
    file = open(join(input_dir, raw_file))
    row_counter = 0
    geo_parser, next_expected_line = reset_state(geo_parser)

    for row in file:
        row_counter += 1
        row = row.strip()
        try:
            if geo_parser.match_row_data_type(next_expected_line, row):
                geo_parser.parse_raw_data(row)
                next_expected_line = next_state(next_expected_line)
            else:
                print(f"[WARNING] At Line {row_counter}")
                print(f"[WARNING] {row} has no match with {next_expected_line}")
                geo_parser, next_expected_line = reset_state(geo_parser)

                # This is tricky, if we had a consistency problem, the current row
                # Can be the start of a new Geographic point. This piece of code
                # Ensures that it will be considered as first point
                # (even when it wasn't expected)
                if geo_parser.match_row_data_type(next_expected_line, row):
                    geo_parser.parse_raw_data(row)
                    next_expected_line = next_state(next_expected_line)
        except Exception as e:
            print(f"[ERROR] at line {row_counter}")
            print(str(e))
            geo_parser, next_expected_line = reset_state(geo_parser)

        if geo_parser.is_complete():
            geo_point = geo_parser.get_geo_point()
            geo_parser, next_expected_line = reset_state(geo_parser)
