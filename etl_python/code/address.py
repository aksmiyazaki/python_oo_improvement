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
            if self.country == "":
                self.country = None

            self.region = geopy_location.raw['Region'].strip()
            if self.region == "":
                self.region = None

            self.city = geopy_location.raw['City'].strip()
            if self.city == "":
                self.city = None

            self.district = geopy_location.raw['District'].strip()
            if self.district == "":
                self.district = None

            self.postal_code = geopy_location.raw['Postal'].strip()
            if self.postal_code == "":
                self.postal_code = None

            self.number = geopy_location.raw['AddNum'].strip()
            if self.number == "":
                self.number = None

            if self.number is not None and self.number != "" and self.number != 0:
                self.street = geopy_location.raw['Address'].split(geopy_location.raw['AddNum'])[0].strip()
            else:
                self.street = geopy_location.raw['Address']

            if self.street == "":
                self.street = None
                
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
            self.__db.execute(sql, params)
        except IntegrityError as e:
            pass
        except Exception as e:
            print(str(e))

    def persist_address(self):
        """
        This method persists Address in a star schema.
        """
        self.__db = DatabaseService.get_instance()

        # If there's more than one occurence of the same lat/lon, just add one to Occurence.
        sql = f"""Select Latitude, Longitude from Address
                where Latitude = {self.latitude} and Longitude = {self.longitude}"""
        res = self.__db.execute_select(sql)
        if len(res) > 0:
            print(f"Latitude = {self.latitude} and Longitude = {self.longitude} returned more than once.")
            sql = f"""Update Address set Occurences =
                        ((Select Occurences from Address where
                        Latitude = {self.latitude} and Longitude = {self.longitude})
                         + 1)
                         where Latitude = {self.latitude} and Longitude = {self.longitude}"""
            res = self.__db.execute(sql)
            self.__db.commit_changes
        else:
            # Adds content to tables
            # Since the data depends on a third party API, we must expect that stuff may be null.
            if self.country is not None and self.country != "":
                sql_ins = "INSERT INTO Country (CountryName) Values (?);"
                params = (self.country,)
                self.__insert_data(sql_ins, params)

            if self.region is not None and self.region != "":
                sql_ins = f"INSERT INTO Region (RegionName) Values (?);"
                params = (self.region,)
                self.__insert_data(sql_ins, params)

            if self.city is not None and self.city != "":
                sql_ins = f"INSERT INTO City (CityName) Values (?);"
                params = (self.city,)
                self.__insert_data(sql_ins, params)

            if self.district is not None and self.district != "":
                sql_ins = f"INSERT INTO District (DistrictName) Values (?)"
                params = (self.district,)
                self.__insert_data(sql_ins, params)

            if self.postal_code is not None and self.postal_code != "":
                sql_ins = f"INSERT INTO Street (PostalCode, StreetName) Values (?,?);"
                params = (self.postal_code, self.street,)
                self.__insert_data(sql_ins, params)

            sql_ins = f"""INSERT INTO Address (Latitude, Longitude, Number, PostalCode,
                          CountryName, DistrictName, RegionName, CityName, Occurences) Values (?, ?, ?, ?, ?, ?, ?, ?, ?)
                          """
            params = (self.latitude, self.longitude, self.number,
            self.postal_code, self.country, self.district, self.region, self.city, 1)

            self.__db.execute(sql_ins, params)
            self.__db.commit_changes()
