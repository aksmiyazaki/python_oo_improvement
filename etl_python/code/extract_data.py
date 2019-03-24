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

for raw_file in data_list:
    raw_file = data_list[0]
    file = open(join(input_dir, raw_file))
    row_counter = 0
    for row in file:
        row_counter += 1
        row = row.strip()
        try:
            geo_parser.parse_raw_data(row)
        except Exception as e:
            print(f"[ERROR] at line {row_counter}")
            geo_parser.reset()
            if geo_parser.match_row_data_type(geoparse.GeoParserState.SEEK_LAT, row):
                geo_parser.parse_raw_data(row)
        if geo_parser.is_complete():
            geo_point = geo_parser.get_geo_point()
            geo_parser.reset()
