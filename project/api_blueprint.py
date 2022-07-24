from flask import Blueprint, request, jsonify
from process import *

data_blueprint = Blueprint("data_blueprint", __name__)

@data_blueprint.route("/scores", methods=["GET"])
def get_data_from_file():
    data = get_data()
    return jsonify(data)


@data_blueprint.route("/scores", methods=["PUT"])
def update_data_in_file():
    data = request.get_json()["result"]
    add_data(data)
    return "OK"
