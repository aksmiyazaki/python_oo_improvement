from geopy.location import Location
from geopy.point import Point
import re
from enum import Enum

class RowDataType(Enum):
    SEEK_LAT = 1
    SEEK_LON = 2
    SEEK_DIST = 3

class GeoParser:
    __raw_lat = None
    __raw_lon = None
    __raw_dist = None
    __lat_regexp = "[-]*[0-9]{1,2}°[0-9]{1,2}′[0-9]{1,2}″[SN]"
    __lon_regexp = "[-]*[0-9]{1,3}°[0-9]{1,2}′[0-9]{1,2}″[WE]"
    __dist_regexp = "[0-9]*.[0-9]* KM"

    def __process_data(self, aim_regex, aim_field, raw_line):
        res = re.search(aim_regex, raw_line)
        if res is not None:
            if aim_field is not None:
                raise Exception(f"[ERROR]   The field is already filled [{aim_field}] [{raw_line}]")
            return res.group(0)
        else:
            return None

    def parse_raw_data(self, raw_line):
        raw_line = raw_line.upper()
        try:
            res = self.__process_data(self.__lat_regexp, self.__raw_lat, raw_line)
            if res is not None:
                self.__raw_lat = res
                return

            res = self.__process_data(self.__lon_regexp, self.__raw_lon, raw_line)
            if res is not None:
                self.__raw_lon = res
                return

            res = self.__process_data(self.__dist_regexp, self.__raw_dist, raw_line)
            if res is not None:
                self.__raw_dist = res.lower()
                return

        except Exception as e:
            print(f"[ERROR] Exception raised on parse_raw_data")
            print(str(e))
            raise

    def is_complete(self):
        return self.__raw_lat is not None and self.__raw_lon is not None and self.__raw_dist is not None

    def get_formatted_raw_data(self):
        return f"{self.__raw_lat} {self.__raw_lon} {self.__raw_dist}"

    def get_geo_point(self):
        if self.is_complete():
            return Point(f"{self.__raw_lat} {self.__raw_lon} {self.__raw_dist}")
        else:
            err_msg = f"""[ERROR]    Can't return point without all data:
                        LAT - {str(self.__raw_lat)} LON - {str(self.__raw_lon)} DIST - {str(self.__raw_dist)}"""
            raise Exception(err_msg)

    def match_row_data_type(self, desired_type, raw_line):
        raw_line = raw_line.upper()
        if desired_type == RowDataType.SEEK_LAT:
            return re.search(self.__lat_regexp, raw_line) is not None
        elif desired_type == RowDataType.SEEK_LON:
            return re.search(self.__lon_regexp, raw_line) is not None
        elif desired_type == RowDataType.SEEK_DIST:
            return re.search(self.__dist_regexp, raw_line)  is not None
        else:
            raise Exception(f"[ERROR]    Couldn't match any type for {desired_type}")

    def reset(self):
        self.__raw_lat = None
        self.__raw_lon = None
        self.__raw_dist = None
