from flask import Flask, request, jsonify
import services


def getAllCountries():
    results = services.getAllCountries()
    
    #Converted list to dictionary
    data = []
    for row in results:
        data.append({"CountryId" : row[0],
                     "Name": row[1],
                     "Population":row[2],
                     "Continent":row[3]})
        
    #return dictionary
    return jsonify(data)


def createCountry(data):
    services.createCountry(data)
    return jsonify({"Message":"Data inserted successfully"})

def deleteCountry(countryID):
    services.deleteCountry(countryID)
    return jsonify({"Message":"Data removed successfully"})