"Initializes the Flask application and configures the blueprint routes."
from flask import Flask
from .routes import main as main_blueprint


def creat_app():
    "Create and configure the Flask application."
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(main_blueprint)

    return app
