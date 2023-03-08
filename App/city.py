from flask import Flask, request, jsonify
import services


def get_all_cities_city():
    results = services.get_all_cities_serv()
    
    #Converted list to dictionary
    data = []
    for row in results:
        data.append({"CityId" : row[0],
                     "Name": row[1],
                     "CountryId":row[2],
                     "Capital":row[3],
                     "FirstLandmark":row[4],
                     "SecondLandmark":row[5],
                     "ThirdLandmark":row[6]
                     })
        
    ##Don't count this SQ return dictionary
    return jsonify(data)


def create_city_city(data):
    services.create_city_serv(data)
    return jsonify({"Message":"City Data inserted successfully"})

def delete_city_city(city_id):
    services.delete_city_serv(city_id)
    return jsonify({"Message":"City Data removed successfully"})

def update_city_city(city_id,data):
    services.update_city_serv(city_id,data)
    return jsonify({"Message":"City Data Updated successfully"})