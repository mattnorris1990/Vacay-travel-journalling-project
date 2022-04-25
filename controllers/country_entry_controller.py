from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import country_repository, place_repository, country_entry_repository, place_entry_repository
from models.country_entry import Country_Entry
from models.country import Country

countryentry_blueprint = Blueprint("countries/entries", __name__)

@countryentry_blueprint.route("/countries/entries/addentry")
def add_country_entry_page():
    countries = country_repository.select_all()

    return render_template('countries/country-entries/add-entry.html', countries = countries)

@countryentry_blueprint.route("/countries/entries/addentry", methods = ['POST'])
def add_country_entry_form():
    title = request.form['entry_title']
    
    if len(request.form['image']) > 0:
        image = request.form['image']
    else:
        image = "images/placeholder_country_image.jpg"
    
    country_id = request.form['country_id']
    country = country_repository.select(country_id)

    text = request.form['entry_text']

    country_entry_object = Country_Entry(title, text, image, country)
    country_entry_repository.save(country_entry_object)

    return redirect (f'/countries/{ country_id }')

@countryentry_blueprint.route('/countries/entries/<id>')
def show_entry(id):
    entry = country_entry_repository.select(id)
    return render_template('/countries/country-entries/show-entry.html', entry = entry)
