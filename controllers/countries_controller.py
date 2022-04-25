from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import country_repository, place_repository, country_entry_repository
from models.country import Country, update_country_visit_status
from models.place import Place
import controllers.places_controller as places_controller

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("/countries/index.html", countries = countries)

@countries_blueprint.route("/addcountry")
def add_country_page():
    return render_template('countries/add-country.html')

@countries_blueprint.route("/addcountry", methods = ['POST'])
def add_country():
    name = request.form['country_name']
    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = "images/placeholder_country_image.jpg"
    
    country_object = Country(name, image)
    country_repository.save(country_object)

    return redirect("/countries")

@countries_blueprint.route('/countries/<id>')
def show_country(id):
    country = country_repository.select(id)
    places = place_repository.select_all()
    entries = country_entry_repository.select_all()
    return render_template('/countries/show-country.html', country=country, places = places, entries=entries)

@countries_blueprint.route("/countries/<id>/edit")
def edit_country_page(id):
    country = country_repository.select(id)
    return render_template('/countries/edit-country.html', country = country)

@countries_blueprint.route('/countries/<id>/edit', methods = ['POST'])
def edit_country_form(id):
    country = country_repository.select(id)
    name = request.form['country_name']
    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = country.image
    country_object = Country(name, image, country.visited, id)
    country_repository.update(country_object)
    return redirect(f'/countries/{ country_object.id }')


@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')


# I want this to redirect to the show_country route, not sure how
@countries_blueprint.route("/countries/<id>/visited", methods= ['POST'])
def update_visited_country(id):
    country_object = country_repository.select(id)
    update_country_visit_status(country_object)
    country_repository.update(country_object)

    return redirect(request.referrer)
