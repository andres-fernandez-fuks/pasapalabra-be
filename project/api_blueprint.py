from flask import Blueprint, request, jsonify
from process import *

data_blueprint = Blueprint("data_blueprint", __name__)

@data_blueprint.route("/", methods=["GET"])
def get_health():
    return "Health ok"

@data_blueprint.route("/scores", methods=["GET"])
def get_data_from_file():
    data = get_data()
    return jsonify(data)


@data_blueprint.route("/scores", methods=["PUT"])
def update_data_in_file():
    data = request.get_json()["result"]
    log_data = request.get_json()["log"]
    add_data(data)
    update_log(log_data)
    return "OK"


@data_blueprint.route("/empty-scores", methods=["POST"])
def empty_scores_file():
    empty_scores()
    return "OK"


@data_blueprint.route("/empty-log", methods=["POST"])
def empty_log_file():
    empty_log()
    return "OK"


@data_blueprint.route("/log", methods=["GET"])
def get_log_file():
    return get_log()