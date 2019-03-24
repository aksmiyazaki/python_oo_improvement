from enum import Enum
from geopy.location import Location
from geopy.point import Point
import re

class GeoParserState(Enum):
    SEEK_LAT = 1
    SEEK_LON = 2
    SEEK_DIST = 3

class GeoParser:
    __raw_lat = None
    __raw_lon = None
    __raw_dist = None
    __lat_regexp = "LATITUDE: [-]*[0-9]{1,2}°[0-9]{1,2}′[0-9]{1,2}″[SN]"
    __lon_regexp = "LONGITUDE: [-]*[0-9]{1,3}°[0-9]{1,2}′[0-9]{1,2}″[WE]"
    __dist_regexp = "DISTANCE: [0-9]*.[0-9]* KM"
    __parser_state = GeoParserState.SEEK_LAT

    def __remove_prefix(self, raw_data):
        return raw_data[raw_data.index(':') + 2:]

    def __process_data(self, aim_regex, aim_field, raw_line):
        res = re.search(aim_regex, raw_line)
        if res is not None:
            if aim_field is not None:
                raise Exception("[ERROR]    {self.__parser_state} expected something that isn't in the raw string {raw_line}")
            aim_field = self.__remove_prefix(res.group(0))

    def parse_raw_data(self, raw_line):
        try:
            raw_line = raw_line.upper()
            aimed_regex = None
            aimed_field = None
            next_state = None
            if self.__parser_state == GeoParserState.SEEK_LAT:
                aimed_regex = self.__lat_regexp
                aimed_field = self.__raw_lat
                next_state = GeoParser.SEEK_LON
            elif self.__parser_state == GeoParserState.SEEK_LON:
                aimed_regex = self.__lon_regexp
                aimed_field = self.__raw_lon
                next_state = GeoParser.SEEK_DIST
            else:
                aimed_regex = self.__dist_regexp
                aimed_field = self.__raw_dist
                next_state = GeoParser.SEEK_LAT

            self.__process_data(aimed_regex, aimed_field, raw_line)

            res = re.search(self.__lat_regexp, raw_line)
            if res is not None:
                if self.__raw_lat is not None:
                    raise Exception("[ERROR]    Latitude is already filled.")
                self.__raw_lat = self.__remove_prefix(res.group(0))
                return

            res = re.search(self.__lon_regexp, raw_line)
            if res:
                if self.__raw_lon is not None:
                    raise Exception("[ERROR]    Longitude is already filled.")
                self.__raw_lon = self.__remove_prefix(res.group(0))
                return

            res = re.search(self.__dist_regexp, raw_line)
            if res:
                if self.__raw_dist is not None:
                    raise Exception("[ERROR]    Distance is already filled.")
                self.__raw_dist = self.__remove_prefix(res.group(0).lower())
                return

            raise Exception("[ERROR]  Couldn't find any defined regex for line {raw_line}")
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

    def reset(self):
        self.__raw_lat = None
        self.__raw_lon = None
        self.__raw_dist = None
        __parser_state = GeoParserState.SEEK_LAT
