from flask import Flask, render_template, Blueprint, request, redirect
from repositories import country_repository, place_repository
from models.country import Country
from models.place import Place

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)