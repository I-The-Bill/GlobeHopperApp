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


def get_all_countries_from_continent_coun(Continent):
    results = services.get_all_countries_from_continent_serv(Continent)
    data = []
    for row in results:
        data.append({"Name":row[0]})
    return jsonify(data)

def get_capital_from_country_coun(countryName):
    results = services.get_capital_from_country_coun_serv(countryName)
    data = []
    for row in results:
        data.append({"Name":row[0],
                     "Country":row[1],
                     "Continent":row[2],
                     "First Landmark":row[3],
                     "Second Landmark":row[4],
                     "Third Landmark":row[5]
                    }) 
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