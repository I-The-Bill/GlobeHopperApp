#Define all services for Country and City

from flask import Flask, request, jsonify
import conn 

##DON"T COUNT THIS SQ mycursor = conn.myconn.cursor()

#get all country records from country table
def get_all_countries():
    
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

def create_country(data):
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

def delete_country(country_id_to_delete):
    #Open connection to SQL
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Stuff to execute
    mysql = "Delete from country where CountryId = %s"
    mycursor.execute(mysql,(country_id_to_delete,))

    #Close the connection
    mycursor.close()
    conn.myconn.close()

