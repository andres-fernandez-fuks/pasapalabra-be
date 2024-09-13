from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
cors = CORS()

FLASK_FILE_NAME = "flask.cfg"


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@pasapalabra_db:5432/pasapalabra"
    initialize_extensions(app)
    register_blueprints(app)
    cors.init_app(app)
    return app


def register_blueprints(app):
    from project.blueprints.api_blueprint import data_blueprint

    app.register_blueprint(data_blueprint)


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    cors.init_app(app)
