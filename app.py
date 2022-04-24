from re import template
from flask import Flask
from controllers.countries_controller import countries_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
