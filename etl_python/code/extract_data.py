import argparse
from os import listdir
from os.path import join

args = None
input_dir = None

parser = argparse.ArgumentParser(description='Read raw data files and parse its contents')
parser.add_argument('--ip', type=str, nargs='+', help='Input path of the raw_data files.')
args = parser.parse_args()


if args == None:
    input_dir = 'C:\\Users\\aksmi\\OneDrive\\Documentos\\GIT\\python_oo_improvement\\etl_python\\raw_data'

data_list = listdir(input_dir)

for raw_file in data_list:
    with open(join(input_dir, raw_file))
