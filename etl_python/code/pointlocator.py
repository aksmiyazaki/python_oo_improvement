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

    @staticmethod
    def get_instance():
        """
        Gets a singleton instance of the class.
        """
        if PointLocator.__instance is None:
            PointLocator()
        return PointLocator.__instance

    def find_point(self, point):
        """
        Method that, given a point, returns its raw location.
        Returns a Geopy Location.
        Keyword arguments:
        point -- A Geopy Point object
        """
        self.__cur_point = point
        self.__decoded_point = self.__coord_decoder.reverse(self.__cur_point, exactly_one=True, timeout=300)

        if self.__decoded_point is not None:
            return self.__decoded_point
        else:
            return None

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
