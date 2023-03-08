#application starting point ie contains main function


from flask import Flask,request,jsonify
import country
app = Flask(__name__)

#READ API (GET)
@app.get("/countries")
def getAllCountries():
    return country.getAllCountries()

#CREATE/UPDATE API (POST)
@app.post("/countries")
def createCountry():
    data = request.json
    return country.createCountry(data)

#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)