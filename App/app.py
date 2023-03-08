#application starting point ie contains main function


from flask import Flask,request,jsonify
from flask_wtf.csrf import CSRFProtect
import country as country_c
import city
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

#####COUNTRIES#####

#CREATE API (POST)
@app.post("/countries")
def create_country_app():
    data = request.json
    return country_c.create_country_coun(data)

#READ API (GET)
@app.get("/countries")
def get_all_countries_app():
    return country_c.get_all_countries_coun()

#UPDATE (PUT)
@app.put("/countries/<int:country_id>")
def update_country_app(country_id):
    data = request.json
    return country_c.update_country_coun(country_id,data)

#DELETE 
@app.delete("/countries/<int:country_id>")
def delete_country_app(country_id):
    return country_c.delete_country_coun(country_id)


#READ API (GET)
@app.get("/countries/<string:Continent>")
def get_all_countries_from_continent_app(Continent):
    return country_c.get_all_countries_from_continent_coun(Continent)


#####CITIES#####


#CREATE API (POST)
@app.post("/cities")
def create_city_app_app():
    data = request.json
    return city.create_city_city(data)

#READ API (GET)
@app.get("/cities")
def get_all_cities_app():
    return city.get_all_cities_city()

#UPDATE (PUT)
@app.put("/cities/<int:city_id>")
def update_city_app(city_id):
    data = request.json
    return city.update_city_city(city_id,data)

#DELETE 
@app.delete("/cities/<int:city_id>")
def delete_city_app(city_id):
    return city.delete_city_city(city_id)




#####JOINED######

@app.get("/countries/<country>/1")
def get_captial_from_country_app(country):
    return country_c.get_capital_from_country_coun(country)




#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)


