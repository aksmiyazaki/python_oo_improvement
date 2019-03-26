from os import chdir
chdir('/home/aksmiyazaki/git/python_oo_improvement/etl_python/code')

from geopy.location import Location
from geopy.point import Point
from geopy.geocoders import ArcGIS
import address

class PointLocator:
    """
    Class that given a point, find a Geopy Location.
    This object has data regarding country, district, address, postal code, etc.
    This class is also implemented using the Singleton Design pattern, since it
    uses an external API that has limitations.
    """
    __instance = None
    __cur_point = None
    __coord_decoder = None
    __decoded_point = None

    @property
    def CurrentPoint(self):
        """
        Gets the current point to be located.
        """
        return self.__cur_point

    @CurrentPoint.setter
    def CurrentPoint(self, value):
        """
        Sets the current point to be located.
        """
        self.__cur_point = value

    @staticmethod
    def get_instance():
        """
        Gets a singleton instance of the class.
        """
        if PointLocator.__instance is None:
            PointLocator()
        return PointLocator.__instance

    def locate_point(self):
        """
        Method that locates the CurrentPoint.
        Is assigns the result to a private attribute.
        """
        self.__decoded_point = self.__coord_decoder.reverse(self.__cur_point, exactly_one=True, timeout=300)

    def __init__(self):
        """
        Object constructor.
        The whole class works as a Singleton, if the program tries to construct
        This class twice, it will trigger an Exception
        """
        if PointLocator.__instance is not None:
            raise Exception("PointLocator is a singleton class. Try GetInstance instead of constructing a new object.")
        else:
            PointLocator.__instance = self
            self.__coord_decoder = ArcGIS()

    def get_located_point(self):
        """
        Gets the decoded point.
        """
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
