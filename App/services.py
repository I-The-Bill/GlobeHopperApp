#Define all services for Country and City

from flask import Flask, request, jsonify
import conn 

##DON"T COUNT THIS SQ mycursor = conn.myconn.cursor()

#get all country records from country table
def get_all_countries_serv():
    
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    mycursor.execute("Select * from Country")
    results = mycursor.fetchall()

    #Close the connection
    mycursor.close()
    conn.myconn.close()

    #Return
    return results

def create_country_serv(data):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    country_id = data['CountryId']
    name = data['Name']
    pop = data['Population']
    cont = data['Continent']
    values = (country_id,name,pop,cont)

    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s)"
    mycursor.execute(mysql,values)

    #Close the connection
    mycursor.close()
    conn.myconn.close()

def delete_country_serv(country_id_to_delete):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    mysql = "Delete from country where CountryId = %s"
    mycursor.execute(mysql,(country_id_to_delete,))

    #Close the connection
    mycursor.close()
    conn.myconn.close()

def update_country_serv(country_id,data):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    name = data['Name']
    pop = data['Population']
    cont = data['Continent']
    values = (country_id,name,pop,cont,country_id)

    mysql = "Update Country set CountryId = %s, Name = %s, Population = %s, Continent = %s where CountryId = %s;"
    mycursor.execute(mysql,values)

    #Close the connection
    mycursor.close()
    conn.myconn.close()




#####CITES#####



def get_all_cities_serv():
    
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    mycursor.execute("Select * from city")
    results = mycursor.fetchall()

    #Close the connection
    mycursor.close()
    conn.myconn.close()

    #Return
    return results

def create_city_serv(data):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    city_id = data['CityId']
    name = data['Name']
    country_id = data['CountryId']
    capital = data['Capital']
    first_landmark = data['FirstLandmark']
    second_landmark = data['SecondLandmark']
    third_landmark = data['ThirdLandmark']
    values = (city_id,name,country_id,capital,first_landmark,second_landmark,third_landmark)

    mysql = "INSERT INTO City (CityId,Name,CountryId,Capital,FirstLandmark,SecondLandmark,ThirdLandmark) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(mysql,values)

    #Close the connection
    mycursor.close()
    conn.myconn.close()

def delete_city_serv(city_id_to_delete):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    mysql = "Delete from City where CityId = %s"
    mycursor.execute(mysql,(city_id_to_delete,))

    #Close the connection
    mycursor.close()
    conn.myconn.close()

def update_city_serv(city_id,data):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    name = data["Name"]
    country_id = data["CountryId"]
    capital = data["Capital"]
    first_landmark = data["FirstLandmark"]
    second_landmark = data["SecondLandmark"]
    third_landmark = data["ThirdLandmark"]
    values = (city_id,name,country_id,capital,first_landmark,second_landmark,third_landmark,city_id)

    mysql = "Update City set CityId = %s, Name = %s, CountryId = %s,Capital = %s,FirstLandmark = %s,SecondLandmark = %s,ThirdLandmark = %s where CityId = %s;"
    mycursor.execute(mysql,values)

    #Close the connection
    mycursor.close()
    conn.myconn.close()
