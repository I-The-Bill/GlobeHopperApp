#application starting point ie contains main function


from flask import Flask,request,jsonify
#from flask_wtf.csrf import CSRFProtect
import country

app = Flask(__name__)
#csrf = CSRFProtect()
#csrf.init_app(app)

#READ API (GET)
@app.get("/countries")
def getAllCountries():
    return country.getAllCountries()

#CREATE/UPDATE API (POST)
@app.post("/countries")
def createCountry():
    data = request.json
    return country.createCountry(data)

@app.delete("/countries/<int:country_id>")
def deleteCountry(country_id):
    return country.deleteCountry(country_id)

#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)