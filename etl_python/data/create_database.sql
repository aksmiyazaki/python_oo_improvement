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
  Latitude FLOAT NOT NULL,
  Longitude FLOAT NOT NULL,
  Number INT,
  Occurences INT NOT NULL,
  PostalCode VARCHAR(255),
  CountryName VARCHAR(255),
  DistrictName VARCHAR(255),
  RegionName VARCHAR(255),
  CityName VARCHAR(255),
  PRIMARY KEY (Latitude, Longitude),
  FOREIGN KEY (PostalCode) REFERENCES Street(PostalCode),
  FOREIGN KEY (CountryName) REFERENCES Country(CountryName),
  FOREIGN KEY (DistrictName) REFERENCES District(DistrictName),
  FOREIGN KEY (RegionName) REFERENCES Region(RegionName),
  FOREIGN KEY (CityName) REFERENCES City(CityName)
);
