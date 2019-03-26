CREATE TABLE Street
(
  StreetName VARCHAR(255) NOT NULL,
  PostalCode VARCHAR(255) NOT NULL,
  PRIMARY KEY (PostalCode)
);

CREATE TABLE District
(
  DistrictId INT NOT NULL AUTOINCREMENT,
  DistrictName VARCHAR(255) NOT NULL,
  PRIMARY KEY (DistrictId)
);

CREATE TABLE City
(
  CityId INT NOT NULL AUTOINCREMENT,
  CityName VARCHAR(255) NOT NULL,
  PRIMARY KEY (CityId)
);

CREATE TABLE Region
(
  RegionId INT NOT NULL AUTOINCREMENT,
  RegionName VARCHAR(255) NOT NULL,
  PRIMARY KEY (RegionId)
);

CREATE TABLE Country
(
  CountryId INT NOT NULL AUTOINCREMENT,
  CountryName VARCHAR(255) NOT NULL,
  PRIMARY KEY (CountryId)
);

CREATE TABLE Address
(
  Latitude INT NOT NULL,
  Longitude INT NOT NULL,
  Number INT NOT NULL,
  AddresId INT NOT NULL AUTOINCREMENT,
  PostalCode INT NOT NULL,
  CountryId INT NOT NULL,
  RegionId INT NOT NULL,
  CityId INT NOT NULL,
  DistrictId INT NOT NULL,
  PRIMARY KEY (AddresId),
  FOREIGN KEY (PostalCode) REFERENCES Street(PostalCode),
  FOREIGN KEY (CountryId) REFERENCES Country(CountryId),
  FOREIGN KEY (RegionId) REFERENCES Region(RegionId),
  FOREIGN KEY (CityId) REFERENCES City(CityId),
  FOREIGN KEY (DistrictId) REFERENCES District(DistrictId)
);
