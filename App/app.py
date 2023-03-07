#application starting point ie contains main function


from flask import Flask,request,jsonify
import country
app = Flask(__name__)

#Read API (GET)
@app.get("/countries")
def getAllCountries():
    return country.getAllCountries()

#Exicute on the terminal as a script
if __name__ == '__main__':
    app.run()