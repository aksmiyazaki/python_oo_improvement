import argparse
from os import listdir
from os.path import join
from os import getcwd
import geoparse
from database import DatabaseService
from pointlocator import PointLocator
from address import Address

args = None
input_dir = None
database_path = None

parser = argparse.ArgumentParser(description='Read raw data files and parse its contents')
parser.add_argument("path", help='Input path of the raw_data files.')
parser.add_argument('db', help='Complete path of .db file (sqlite database). Example: ../data/database.db')
args = parser.parse_args()

if args == None:
    input_dir = '/home/aksmiyazaki/git/python_oo_improvement/etl_python/raw_data'
    database_path = '../data/database.db'
else:
    input_dir = str(args.path)
    database_path = str(args.db)

print(f"Running with the following arguments: [{input_dir}] [{database_path}]")
input()

db = DatabaseService.get_instance()
db.initialize_database_conn(database_path)
data_list = listdir(input_dir)
geo_point = None
geo_parser = geoparse.GeoParser()
locator = PointLocator.get_instance()

def next_state(cur_state):
    if cur_state == geoparse.RowDataType.SEEK_LAT:
        return geoparse.RowDataType.SEEK_LON
    elif cur_state == geoparse.RowDataType.SEEK_LON:
        return geoparse.RowDataType.SEEK_DIST
    elif cur_state == geoparse.RowDataType.SEEK_DIST:
        return geoparse.RowDataType.SEEK_LAT
    else:
        raise Exception(f"[ERROR]   There is no next state for current {cur_state}")

def reset_state(parser):
    parser.reset()
    return parser, geoparse.RowDataType.SEEK_LAT

for raw_file in data_list:
    row_counter = 0
    geo_parser, next_expected_line = reset_state(geo_parser)
    print(f"Openning file {join(input_dir, raw_file)}")
    input()
    with open(join(input_dir, raw_file)) as file:
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

                    if geo_parser.match_row_data_type(next_expected_line, row):
                        geo_parser.parse_raw_data(row)
                        next_expected_line = next_state(next_expected_line)
            except Exception as e:
                print(f"[ERROR] at line {row_counter}")
                print(str(e))
                geo_parser, next_expected_line = reset_state(geo_parser)

            if geo_parser.is_complete():
                geo_point = geo_parser.get_geo_point()
                print(f"Completed geo point: {geo_point}")
                input()
                found_point = locator.find_point(geo_point)
                print(f"Found: {found_point}")
                input()
                adr = Address(found_point)
                adr.persist_address()
                input()
                geo_parser, next_expected_line = reset_state(geo_parser)
