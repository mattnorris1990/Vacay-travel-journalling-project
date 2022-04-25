from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import country_repository, place_repository
from models.country import Country
from models.place import Place, update_place_visit_status

places_blueprint = Blueprint("countries/places", __name__)

@places_blueprint.route("/countries/places/addplace")
def add_place_page():
    countries = country_repository.select_all()
    return render_template('countries/places/add-place.html', countries = countries)

@places_blueprint.route('/countries/places/addplace', methods = ['POST'])
def add_place_form():
    name = request.form['place_name']
    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = "images/placeholder_country_image.jpg"
    
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    
    place_object = Place(name, country, image)
    place_repository.save(place_object)

    return redirect (f'/countries/{ country_id }')

@places_blueprint.route('/countries/places/<id>')
def show_place(id):
    place = place_repository.select(id)
    return render_template('countries/places/show-place.html', place = place)

@places_blueprint.route('/countries/places/<id>/delete', methods = ['POST'])
def delete_place(id):
    place_object = place_repository.select(id)
    country_id = place_object.country.id
    place_repository.delete(id)

    return redirect(f'/countries/{ country_id }')

@places_blueprint.route('/countries/places/<id>/edit')
def edit_place_page(id):
    place = place_repository.select(id)
    return render_template('countries/places/edit-place.html', place = place)

@places_blueprint.route('/countries/places/<id>/edit', methods = ['POST'])
def edit_place_form(id):
    place = place_repository.select(id)
    name = request.form['place_name']
    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = place.image

    country_id = place.country.id
    country = country_repository.select(country_id)
    
    place_object = Place(name, country, image, place.visited, id)
    place_repository.update(place_object)

    return redirect(f'/countries/{ country_id }')

@places_blueprint.route("/countries/places/<id>/visited", methods= ['POST'])
def update_visited_place(id):
    place_object = place_repository.select(id)
    update_place_visit_status(place_object)
    place_repository.update(place_object)
    print(place_object)
    return redirect(request.referrer)


