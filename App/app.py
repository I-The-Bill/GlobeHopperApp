#application starting point ie contains main function


from flask import Flask,request,jsonify
from flask_wtf.csrf import CSRFProtect
import country

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

#READ API (GET)
@app.get("/countries")
def get_all_countries():
    return country.get_all_countries()

#CREATE/UPDATE API (POST)
@app.post("/countries")
def create_country():
    data = request.json
    return country.create_country(data)

@app.delete("/countries/<int:country_id>")
def delete_country(country_id):
    return country.delete_country(country_id)

@app.put("/countries/<int:country_id>")
def update_country(country_id):
    data = request.json
    return country.update_country(country_id,data)

#Execute on the terminal as a script
if __name__ == '__main__':
    app.run(debug=True)