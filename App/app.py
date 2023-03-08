#application starting point ie contains main function


from flask import Flask,request,jsonify
##from flask_wtf.csrf import CSRFProtect
import country
import city
app = Flask(__name__)
##csrf = CSRFProtect()
##csrf.init_app(app)

#####COUNTRIES#####

#CREATE API (POST)
@app.post("/countries")
def create_country_app():
    data = request.json
    return country.create_country_coun(data)

#READ API (GET)
@app.get("/countries")
def get_all_countries_app():
    return country.get_all_countries_coun()

#UPDATE (PUT)
@app.put("/countries/<int:country_id>")
def update_country_app(country_id):
    data = request.json
    return country.update_country_coun(country_id,data)

#DELETE 
@app.delete("/countries/<int:country_id>")
def delete_country_app(country_id):
    return country.delete_country_coun(country_id)


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

#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)