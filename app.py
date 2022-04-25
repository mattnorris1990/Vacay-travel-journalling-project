from re import template
from flask import Flask
from controllers.countries_controller import countries_blueprint
from controllers.places_controller import places_blueprint
from controllers.country_entry_controller import countryentry_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(places_blueprint)
app.register_blueprint(countryentry_blueprint)
