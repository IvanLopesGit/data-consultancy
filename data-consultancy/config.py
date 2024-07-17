"Configuration settings for the Flask application."
import os


class Config:
    "Class for configuration settings."
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
