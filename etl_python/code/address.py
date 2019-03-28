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
    __db = None
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
            self.region = geopy_location.raw['Region'].strip()
            self.city = geopy_location.raw['City'].strip()
            self.district = geopy_location.raw['District'].strip()
            self.postal_code = geopy_location.raw['Postal'].strip()
            self.number = geopy_location.raw['AddNum'].strip()
            if self.number is not None and self.number != "" and self.number != 0:
                self.street = geopy_location.raw['Address'].split(geopy_location.raw['AddNum'])[0].strip()
            else:
                print("Number is none")
                self.street = geopy_location.raw['Address']
        except Exception as e:
            print(f"Error parsing object")
            print(str(e))
            print(f"{str(geopy_location.raw)}")
            input()

    def __insert_data(self, sql, params = None):
        """
        Method that inserts data into the database
        If an IntegrityError is raised as exception, considers that it is
        a unique constraint violation and moves on
        Keyword arguments:
        sql -- An insert sql.
        params -- Parameters of the insert.
        """
        try:
            self.__db.execute_insert(sql, params)
        except IntegrityError as e:
            pass
        except Exception as e:
            print(str(e))

    def persist_address(self):
        """
        This method persists Address in a star schema.
        """
        self.__db = DatabaseService.get_instance()

        sql_ins = "INSERT INTO Country (CountryName) Values (?);"
        params = (self.country,)
        self.__insert_data(sql_ins, params)

        sql_ins = f"INSERT INTO Region (RegionName) Values (?);"
        params = (self.region,)
        self.__insert_data(sql_ins, params)

        sql_ins = f"INSERT INTO City (CityName) Values (?);"
        params = (self.city,)
        self.__insert_data(sql_ins, params)

        sql_ins = f"INSERT INTO District (DistrictName) Values (?)"
        params = (self.district,)
        self.__insert_data(sql_ins, params)

        sql_ins = f"INSERT INTO Street (PostalCode, StreetName) Values (?,?);"
        params = (self.postal_code, self.street,)
        self.__insert_data(sql_ins, params)

        sql_ins = f"""INSERT INTO Address (Latitude, Longitude, Number, PostalCode,
                      CountryName, DistrictName, RegionName, CityName) Values (?, ?, ?, ?, ?, ?, ?, ?)
                      """
        params = (self.latitude, self.longitude, self.number,
        self.postal_code, self.country, self.district, self.region, self.city,)

        self.__db.execute_insert(sql_ins, params)
        self.__db.commit_changes()
