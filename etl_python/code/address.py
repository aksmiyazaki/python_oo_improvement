import pycountry_convert
from database import DatabaseService
from geopy.location import Location
from sqlite3 import IntegrityError

class Address:
    """
    his class represents an address
    It has a set of attributes that composes the object such as latitude, Longitude
    street, number, district, etc.
    """
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
        """
        Class constructor, initializes address attributes.
        Keyword arguments:
        geopy_location -- a GeoPy location with raw data to be converted into as
        Address object.
        """
        try:
            self.latitude = geopy_location.latitude
            self.longitude = geopy_location.longitude
            self.country = pycountry_convert.map_country_alpha3_to_country_name()[geopy_location.raw['CountryCode']].strip()
            self.number = geopy_location.raw['AddNum'].strip()
            self.district = geopy_location.raw['District'].strip()
            self.city = geopy_location.raw['City'].strip()
            self.postal_code = geopy_location.raw['Postal'].strip()
            self.street = geopy_location.raw['Address'].split(geopy_location.raw['AddNum'])[0].strip()
            self.region = geopy_location.raw['Region'].strip()
        except Exception as e:
            print(f"Error parsing object")
            print(str(e))
            print(f"{str(geopy_location.raw)}")

    def __insert_data(self, sql):
        """
        Method that inserts data into the database
        If an IntegrityError is raised as exception, considers that it is
        a unique constraint violation and moves on
        Keyword arguments:
        sql -- An insert sql.
        """
        try:
            db.execute_insert(sql)
        except IntegrityError as e:
            pass
        except Exception as e:
            print(str(e))

    def persist_address(self):
        """
        This method persists Address in a star schema.
        """
        db = DatabaseService.get_instance()

        sql_ins = f"INSERT INTO Country (CountryName) Values ({self.country});"
        self.__insert_data(sql_ins)

        sql_ins = f"INSERT INTO Region (RegionName) Values ({self.region});"
        self.__insert_data(sql_ins)

        sql_ins = f"INSERT INTO City (CityName) Values ({self.city});"
        self.__insert_data(sql_ins)

        sql_ins = f"INSERT INTO District (DistrictName) Values ({self.district})"
        self.__insert_data(sql_ins)

        sql_ins = f"INSERT INTO Street (PostalCode, StreetName) Values ({self.postal_code}, {self.street});"
        self.__insert_data(sql_ins)

        sql_ins = f"""INSERT INTO Address (Latitude, Longitude, Number, PostalCode,
                      CountryName, DistrictName, RegionName, CityName) Values
                      ({self.latitude}, {self.longidute}, {self.number},
                      {self.postal_code}, {self.country}, {self.district}, {self.region},
                      {self.city})
                   """
        db.execute_insert(sql_ins)
