from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import place_repository, place_entry_repository
from models.place_entry import Place_Entry
from models.place import Place
from models.country import Country

placeentry_blueprint = Blueprint("countries/places/entries", __name__)

@placeentry_blueprint.route("/countries/places/entries/addentry")
def add_place_entry_page():
    places = place_repository.select_all()

    return render_template('countries/places/place-entries/add-entry.html', places = places)

@placeentry_blueprint.route("/countries/places/entries/addentry", methods = ['POST'])
def add_place_entry_form():
    title = request.form['entry_title']
    
    place_id = request.form['place_id']
    place = place_repository.select(place_id)

    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = "images/placeholder_country_image.jpg"

    text = request.form['entry_text']

    place_entry_object = Place_Entry(title, text, image, place)
    place_entry_repository.save(place_entry_object)

    return redirect (f'/countries/places/{ place_id }')