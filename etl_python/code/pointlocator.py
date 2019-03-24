from os import chdir
chdir('/home/aksmiyazaki/git/python_oo_improvement/etl_python/code')

from geopy.location import Location
from geopy.point import Point
from geopy.geocoders import ArcGIS
import address

class PointLocator:
    __instance = None
    __cur_point = None
    __coord_decoder = None
    __decoded_point = None

    @property
    def CurrentPoint(self):
        return self.__cur_point

    @CurrentPoint.setter
    def CurrentPoint(self, value):
        self.__cur_point = value

    @staticmethod
    def get_instance():
        if PointLocator.__instance is None:
            PointLocator()
        return PointLocator.__instance

    def locate_point(self):
        self.__decoded_point = self.__coord_decoder.reverse(self.__cur_point, exactly_one=True, timeout=300)

    def __init__(self):
        if PointLocator.__instance is not None:
            raise Exception("PointLocator is a singleton class. Try GetInstance instead of constructing a new object.")
        else:
            PointLocator.__instance = self
            self.__coord_decoder = ArcGIS()

    def get_located_point(self):
        if self.__decoded_point is not None:
            return self.__decoded_point
        else:
            return None

p = PointLocator()
p.CurrentPoint = Point("30°02′59″S 51°12′05″W 2.2959 km")
p.locate_point()
lp = p.get_located_point()
addr = address.Address(lp)
lp.raw
