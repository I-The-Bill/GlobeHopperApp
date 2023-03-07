#Define all services for Country and City

from flask import Flask, request, jsonify
import conn 

## mycursor = conn.myconn.cursor()

#get all country records from country table using sql
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
