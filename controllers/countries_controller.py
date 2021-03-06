from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import country_repository, place_repository, country_entry_repository
from models.country import *
from models.place import Place
from services.services import *
import controllers.places_controller as places_controller

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    entries = country_entry_repository.select_all()
    return render_template("/countries/index.html", countries = countries, entries = entries, stylesheet="stylesheet.css'")

@countries_blueprint.route("/countries/visited")
def countries_visited():
    all_countries = country_repository.select_all()
    countries = check_visit_status_true(all_countries)
    entries = country_entry_repository.select_all()
    return render_template("/countries/index.html", countries = countries, entries = entries)

@countries_blueprint.route("/countries/wishlist")
def countries_wishlist():
    all_countries = country_repository.select_all()
    countries = check_visit_status_false(all_countries)
    entries = country_entry_repository.select_all()
    return render_template("/countries/index.html", countries = countries, entries = entries)

@countries_blueprint.route("/countries", methods=['POST'])
def countries_by_continent():
    all_countries = country_repository.select_all()
    continent = request.form["continent"]
    countries = check_continent(all_countries, continent)
    entries = country_entry_repository.select_all()
    return render_template("/countries/index.html", countries = countries, entries = entries)

@countries_blueprint.route("/addcountry")
def add_country_page():
    return render_template('countries/add-country.html')

@countries_blueprint.route("/addcountry", methods = ['POST'])
def add_country():
    name = request.form['country_name']
    image = new_country_check_for_image_input(request.form['image'])
    continent = request.form['continent']
    
    country_object = Country(name, image, continent)
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
    image = edit_country_check_for_image_input(request.form['image'], country)
    country_object = Country(name, image, country.continent, country.visited, id)
    country_repository.update(country_object)
    return redirect(f'/countries/{ country_object.id }')


@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')



@countries_blueprint.route("/countries/<id>/visited", methods= ['POST'])
def update_visited_country(id):
    country_object = country_repository.select(id)
    update_country_visit_status(country_object)
    country_repository.update(country_object)

    return redirect(request.referrer)
