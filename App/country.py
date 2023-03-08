from flask import Flask, request, jsonify
import services


def get_all_countries_coun():
    results = services.get_all_countries_serv()
    
    #Converted list to dictionary
    data = []
    for row in results:
        data.append({"CountryId" : row[0],
                     "Name": row[1],
                     "Population":row[2],
                     "Continent":row[3]})
        
    ##Don't count this SQ return dictionary
    return jsonify(data)


def create_country_coun(data):
    services.create_country_serv(data)
    return jsonify({"Message":"Data inserted successfully"})

def delete_country_coun(country_id):
    services.delete_country_serv(country_id)
    return jsonify({"Message":"Data removed successfully"})

def update_country_coun(country_id,data):
    services.update_country_serv(country_id,data)
    return jsonify({"Message":"Data Updated successfully"})