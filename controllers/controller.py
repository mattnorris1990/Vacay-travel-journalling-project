from flask import Flask, render_template, Blueprint

home_blueprint = Blueprint("/", __name__)

@home_blueprint.route("/")
def home_page():
    return render_template('index.html', stylesheet='home-stylesheet.css')