from flask import Flask

def creat_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app