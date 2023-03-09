#application starting point ie contains main function


from flask import Flask,request,jsonify
from flask_wtf.csrf import CSRFProtect
import country as country_c
import city




app = Flask(__name__)
'''csrf = CSRFProtect()
csrf.init_app(app)


import os
SECRET_KEY = os.urandom(32)
print(SECRET_KEY)
app.config['SECRET_KEY'] = "bob"'''

#####COUNTRIES#####

#CREATE API (POST)
@app.post("/countries")
#@csrf.exempt
def create_country_app():
    data = request.json
    return country_c.create_country_coun(data)

#READ API (GET)
@app.get("/countries")
#@csrf.exempt
def get_all_countries_app():
    return country_c.get_all_countries_coun()

#UPDATE (PUT)
@app.put("/countries/<int:country_id>")
#@csrf.exempt
def update_country_app(country_id):
    data = request.json
    return country_c.update_country_coun(country_id,data)

#DELETE 
@app.delete("/countries/<int:country_id>")
#@csrf.exempt
def delete_country_app(country_id):
    return country_c.delete_country_coun(country_id)


#READ API (GET)
@app.get("/countries/<string:continent>")
def get_all_countries_from_continent_app(continent):
    return country_c.get_all_countries_from_continent_coun(continent)


#####CITIES#####


#CREATE API (POST)
@app.post("/cities")
#@csrf.exempt
def create_city_app_app():
    data = request.json
    return city.create_city_city(data)

#READ API (GET)
@app.get("/cities")
def get_all_cities_app():
    return city.get_all_cities_city()

#UPDATE (PUT)
@app.put("/cities/<int:city_id>")
#@csrf.exempt
def update_city_app(city_id):
    data = request.json
    return city.update_city_city(city_id,data)

#DELETE 
@app.delete("/cities/<int:city_id>")
#@csrf.exempt
def delete_city_app(city_id):
    return city.delete_city_city(city_id)




#####JOINED######

@app.get("/countries/<country>/1")
def get_captial_from_country_app(country):
    return country_c.get_capital_from_country_coun(country)

@app.get("/countries/size/<int:size>")
def get_countries_from_size_app(size):
    return country_c.get_countries_from_size_app(size)


#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)


