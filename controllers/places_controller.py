from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import country_repository, place_repository
from models.country import Country
from models.place import Place
import controllers.countries_controller as countries_controller

places_blueprint = Blueprint("countries/places", __name__)

@places_blueprint.route("/countries/places/addplace")
def add_place_page():
    countries = country_repository.select_all()
    return render_template('countries/places/add-place.html', countries = countries)

@places_blueprint.route('/countries/places/addplace', methods = ['POST'])
def add_place():
    name = request.form['place_name']
    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = "images/placeholder_country_image.jpg"
    
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    
    place_object = Place(name, country, image)
    place_repository.save(place_object)

    return redirect ('/countries')