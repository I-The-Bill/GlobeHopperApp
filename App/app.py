#application starting point ie contains main function


from flask import Flask,request,jsonify
#Don't count this SQ from flask_wtf.csrf import CSRFProtect
import country

app = Flask(__name__)
##Don't count this SQ csrf = CSRFProtect()
##Don't count this SQ csrf.init_app(app)

#READ API (GET)
@app.get("/countries")
def get_all_countries():
    return country.getAllCountries()

#CREATE/UPDATE API (POST)
@app.post("/countries")
def create_country():
    data = request.json
    return country.createCountry(data)

@app.delete("/countries/<int:country_id>")
def delete_country(country_id):
    return country.deleteCountry(country_id)

#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)