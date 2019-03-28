CREATE TABLE Street
(
  StreetName VARCHAR(255) NOT NULL,
  PostalCode VARCHAR(255) NOT NULL,
  PRIMARY KEY (PostalCode)
);

CREATE TABLE District
(
  DistrictName VARCHAR(255) NOT NULL,
  PRIMARY KEY (DistrictName)
);

CREATE TABLE City
(
  CityName VARCHAR(255) NOT NULL,
  PRIMARY KEY (CityName)
);

CREATE TABLE Region
(
  RegionName VARCHAR(255) NOT NULL,
  PRIMARY KEY (RegionName)
);

CREATE TABLE Country
(
  CountryName VARCHAR(255) NOT NULL,
  PRIMARY KEY (CountryName)
);

CREATE TABLE Address
(
  Latitude INT NOT NULL,
  Longitude INT NOT NULL,
  Number INT NOT NULL,
  AddresId INTEGER PRIMARY KEY AUTOINCREMENT,
  PostalCode VARCHAR(255) NOT NULL,
  CountryName VARCHAR(255) NOT NULL,
  DistrictName VARCHAR(255) NOT NULL,
  RegionName VARCHAR(255) NOT NULL,
  CityName VARCHAR(255) NOT NULL,
  FOREIGN KEY (PostalCode) REFERENCES Street(PostalCode),
  FOREIGN KEY (CountryName) REFERENCES Country(CountryName),
  FOREIGN KEY (DistrictName) REFERENCES District(DistrictName),
  FOREIGN KEY (RegionName) REFERENCES Region(RegionName),
  FOREIGN KEY (CityName) REFERENCES City(CityName)
);
