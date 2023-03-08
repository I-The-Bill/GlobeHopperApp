#Define all services for Country and City

from flask import Flask, request, jsonify
import conn 

## mycursor = conn.myconn.cursor()

#get all country records from country table
def getAllCountries():
    
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

def createCountry(data):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    
    cId = data['CountryId']
    name = data['Name']
    pop = data['Population']
    cont = data['Continent']
    #if data['CountryId'] == null:
     #   cId = data['CountryId']
    values = (cId,name,pop,cont)

    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s)"
    mycursor.execute(mysql,values)

    #Close the connection
    mycursor.close()
    conn.myconn.close()

