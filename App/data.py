import conn

#create curser for the connonction object
myCursor = conn.myconn.cursor()

#Use globehopperapp schemea
myCursor.execute("USE globehopperapp")

myCursor.execute("DROP TABLE IF EXISTS Country")

myCursor.execute("CREATE TABLE Country (CountryId INT AUTO_INCREMENT  PRIMARY KEY, Name VARCHAR(100) NOT NULL,Population DOUBLE NOT NULL,Continent VARCHAR(250) NOT NULL)")

myCursor.execute("DROP TABLE IF EXISTS City")
  
myCursor.execute("CREATE TABLE City (CityId INT AUTO_INCREMENT  PRIMARY KEY, Name VARCHAR(100) NOT NULL, CountryId INT NOT NULL, Capital INT NOT NULL, FirstLandmark VARCHAR(250) NOT NULL, SecondLandmark VARCHAR(250) NOT NULL,ThirdLandmark VARCHAR(250) NOT NULL )")


myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (1, 'Canada', 30000000, 'North America')")
myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (2, 'USA', 330000000, 'North America')")
myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (3, 'France', 3000000, 'Europe')")
myCursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (4, 'India', 300000000, 'Asia')")

myCursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (1, 'Ottawa', 1, 1, 'Parliament House', 'Museum', 'Rideau Canal')")
myCursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (2, 'Toronto', 1, 0, 'CN Tower', 'Niagara Falls', 'AGO')")
myCursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (3, 'Washington', 2, 1, 'White House', 'Lincoln Memorial', 'National Air and Space Museum')")


conn.myconn.commit()