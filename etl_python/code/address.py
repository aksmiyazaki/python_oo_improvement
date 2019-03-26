from os import chdir
chdir('/home/aksmiyazaki/git/python_oo_improvement/etl_python/code')

import pycountry_convert
import database
from geopy.location import Location


class Address:
    """This class represents an address
    It has a set of attributes that composes the object such as latitude, Longitude
    street, number, district, etc."""
    latitude = None
    longitude = None
    street = None
    number = None
    district = None
    city = None
    region = None
    postal_code = None
    country = None

    def __init__(self, geopy_location):
        """ Class constructor, initializes address attributes.
        Keyword arguments:
        geopy_location -- a GeoPy location with raw data to be converted into as
        Address object.
        """
        try:
            self.latitude = geopy_location.latitude
            self.longitude = geopy_location.longitude
            self.street = geopy_location.raw['Address'].split(geopy_location.raw['AddNum'])[0].strip()
            self.number = geopy_location.raw['AddNum'].strip()
            self.district = geopy_location.raw['District'].strip()
            self.city = geopy_location.raw['City'].strip()
            self.postal_code = geopy_location.raw['Postal'].strip()
            self.region = geopy_location.raw['Region'].strip()
            self.country = pycountry_convert.map_country_alpha3_to_country_name()[geopy_location.raw['CountryCode']].strip()
        except Exception as e:
            print(f"Error parsing object")
            print(str(e))
            print(f"{str(geopy_location.raw)}")
