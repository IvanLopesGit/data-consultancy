"Defines the routes for the Flask application."
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    "Render the index page."
    return render_template('home.html')
