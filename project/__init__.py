from flask import Flask
from flask_cors import CORS

cors = CORS()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    register_blueprints(app)
    cors.init_app(app)
    return app

def register_blueprints(app):
    from project.api_blueprint import data_blueprint
    app.register_blueprint(data_blueprint)
