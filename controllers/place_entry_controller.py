from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import place_repository, place_entry_repository
from models.place_entry import Place_Entry
from services.services import *
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

    image = new_entry_check_for_image_input(request.form['image'])

    text = request.form['entry_text']

    place_entry_object = Place_Entry(title, text, image, place)
    place_entry_repository.save(place_entry_object)

    return redirect (f'/countries/places/{ place_id }')

@placeentry_blueprint.route('/countries/places/entries/<id>')
def show_place_entry(id):
    entry = place_entry_repository.select(id)
    place = entry.place

    return render_template('/countries/places/place-entries/show-entry.html', entry = entry, place=place)

@placeentry_blueprint.route('/countries/places/entries/<id>/delete', methods = ['POST'])
def delete_place_entry(id):
    entry_object = place_entry_repository.select(id)
    entry_id = entry_object.place.id
    place_entry_repository.delete(id)

    return redirect(f'/countries/places/{ entry_id }')

@placeentry_blueprint.route('/countries/places/entries/<id>/edit')
def edit_place_entry_page(id):
    entry = place_entry_repository.select(id)
    return render_template('countries/places/place-entries/edit-entry.html', entry = entry)

@placeentry_blueprint.route('/countries/places/entries/<id>/edit', methods = ['POST'])
def edit_place_entry_form(id):
    entry = place_entry_repository.select(id)
    title = request.form['entry_title']
    image = edit_entry_check_for_image_input(request.form['image'], entry)
    text = request.form['entry_text']

    entry_object = Place_Entry(title, text, image, entry.place, entry.date_stamp, id)
    place_entry_repository.update(entry_object)

    return redirect(f'/countries/places/entries/{id}')