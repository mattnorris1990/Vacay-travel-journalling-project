from flask import Flask, render_template, Blueprint, request, redirect, url_for
from repositories import country_repository, place_repository, country_entry_repository, place_entry_repository
from services.services import *
from models.country_entry import CountryEntry
from models.country import Country

countryentry_blueprint = Blueprint("countries/entries", __name__)


@countryentry_blueprint.route("/countries/entries/addentry")
def add_country_entry_page():
    countries = country_repository.select_all()

    return render_template('countries/country-entries/add-entry.html', countries = countries)


@countryentry_blueprint.route("/countries/entries/addentry", methods = ['POST'])
def add_country_entry_form():
    title = request.form['entry_title']
    
    country_id = request.form['country_id']
    country = country_repository.select(country_id)

    image = new_entry_check_for_image_input(request.form['image'])

    text = request.form['entry_text']

    country_entry_object = CountryEntry(title, text, image, country)
    country_entry_repository.save(country_entry_object)

    return redirect (f'/countries/{ country_id }')


@countryentry_blueprint.route('/countries/entries/<id>')
def show_entry(id):
    entry = country_entry_repository.select(id)
    country = entry.country
    return render_template('/countries/country-entries/show-entry.html', entry = entry, country=country)


@countryentry_blueprint.route('/countries/entries/<id>/delete', methods = ['POST'])
def delete_country_entry(id):
    entry_object = country_entry_repository.select(id)
    entry_id = entry_object.country.id
    country_entry_repository.delete(id)

    return redirect(f'/countries/{ entry_id }')


@countryentry_blueprint.route('/countries/entries/<id>/edit')
def edit_country_entry_page(id):
    entry = country_entry_repository.select(id)
    return render_template('countries/country-entries/edit-entry.html', entry = entry)

@countryentry_blueprint.route('/countries/entries/<id>/edit', methods = ['POST'])
def edit_country_entry_form(id):
    entry = country_entry_repository.select(id)
    title = request.form['entry_title']
    image = edit_entry_check_for_image_input(request.form['image'], entry)
    text = request.form['entry_text']

    entry_object = CountryEntry(title, text, image, entry.country, entry.date_stamp, id)
    country_entry_repository.update(entry_object)

    return redirect(f'/countries/entries/{id}')
