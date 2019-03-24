from enum import Enum
from geopy.location import Location
from geopy.point import Point
import re

class GeoParserState(Enum):
    SEEK_LAT = 1
    SEEK_LON = 2
    SEEK_DIST = 3
    RESET_STATE = 4

class GeoParser:
    __raw_lat = None
    __raw_lon = None
    __raw_dist = None
    __lat_regexp = "LATITUDE: [-]*[0-9]{1,2}°[0-9]{1,2}′[0-9]{1,2}″[SN]"
    __lon_regexp = "LONGITUDE: [-]*[0-9]{1,3}°[0-9]{1,2}′[0-9]{1,2}″[WE]"
    __dist_regexp = "DISTANCE: [0-9]*.[0-9]* KM"
    __parser_expected_state = GeoParserState.SEEK_LAT

    @property
    def parser_expected_state(self):
        return self.__parser_expected_state

    def __remove_prefix(self, raw_data):
        return raw_data[raw_data.index(':') + 2:]

    def __process_data(self, aim_regex, aim_field, raw_line):
        res = re.search(aim_regex, raw_line)
        if res is not None:
            if aim_field is not None:
                raise Exception(f"[ERROR]    {self.__parser_expected_state} expected something that isn't in the raw string {raw_line}")
            return self.__remove_prefix(res.group(0))
        else:
            raise Exception(f"[ERROR]    {self.__parser_expected_state} expected something that isn't in the raw string {raw_line}")

    def parse_raw_data(self, raw_line):
        try:
            raw_line = raw_line.upper()

            if self.__parser_expected_state == GeoParserState.SEEK_LAT:
                self.__raw_lat = self.__process_data(self.__lat_regexp, self.__raw_lat, raw_line)
                self.__parser_expected_state = GeoParserState.SEEK_LON
            elif self.__parser_expected_state == GeoParserState.SEEK_LON:
                self.__raw_lon = self.__process_data(self.__lon_regexp, self.__raw_lon, raw_line)
                self.__parser_expected_state = GeoParserState.SEEK_DIST
            else:
                self.__raw_dist = self.__process_data(self.__dist_regexp, self.__raw_dist, raw_line)
                self.__raw_dist = self.__raw_dist.lower()
                self.__parser_expected_state = GeoParserState.RESET_STATE
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
        if desired_type == GeoParserState.SEEK_LAT:
            return re.search(self.__lat_regexp, raw_line) is not None
        elif desired_type == GeoParserState.SEEK_LON:
            return re.search(self.SEEK_LON, raw_line) is not None
        elif desired_type == GeoParserState.SEEK_DIST:
            return re.search(self.SEEK_DIST, raw_line)  is not None
        else:
            raise Exception(f"[ERROR]    Couldn't match any type for {desired_type}")

    def reset(self):
        self.__raw_lat = None
        self.__raw_lon = None
        self.__raw_dist = None
        self.__parser_expected_state = GeoParserState.SEEK_LAT
