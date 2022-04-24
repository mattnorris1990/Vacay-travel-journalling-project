from flask import Flask, render_template, Blueprint, request, redirect
from repositories import country_repository, place_repository
from models.country import Country
from models.place import Place

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
    return render_template('/countries/show-country.html', country=country)

@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')