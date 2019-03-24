from geopy.location import Location
from geopy.point import Point
from geopy.geocoders import ArcGIS

class PointLocator:
    __instance = None
    __cur_point = None
    coord_decoder = None
    decoded_point = None

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

    def LocatePoint(self):
        self.decoded_point = self.coord_decoder.reverse(self.__cur_point, exactly_one=True, timeout=300)


    def __init__(self):
        if PointLocator.__instance is not None:
            raise Exception("PointLocator is a singleton class. Try GetInstance instead of constructing a new object.")
        else:
            PointLocator.__instance = self
            self.coord_decoder = ArcGIS()

p = PointLocator()
pt = Point("30°02′59″S 51°12′05″W 2.2959 km")
p.CurrentPoint = pt
p.LocatePoint()
p.decoded_point
pt.latitude
pt.longitude
pt.altitude
