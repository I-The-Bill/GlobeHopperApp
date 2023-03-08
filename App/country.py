from flask import Flask, request, jsonify
import services


def get_all_countries():
    results = services.get_all_countries()
    
    #Converted list to dictionary
    data = []
    for row in results:
        data.append({"CountryId" : row[0],
                     "Name": row[1],
                     "Population":row[2],
                     "Continent":row[3]})
        
    ##Don't count this SQ return dictionary
    return jsonify(data)


def create_country(data):
    services.create_country(data)
    return jsonify({"Message":"Data inserted successfully"})

def delete_country(country_id):
    services.delete_country(country_id)
    return jsonify({"Message":"Data removed successfully"})

def update_country(country_id,data):
    services.update_country(country_id,data)
    return jsonify({"Message":"Data inserted successfully"})