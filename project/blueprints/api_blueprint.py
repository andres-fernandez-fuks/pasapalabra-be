from flask import Blueprint, request, jsonify
from project.helpers.process import *
from project.models.log import Log
from project.models.score import Score

data_blueprint = Blueprint("data_blueprint", __name__)

@data_blueprint.route("/", methods=["GET"])
def get_health():
    return "Health ok"

@data_blueprint.route("/scores", methods=["GET"])
def get_players_scores():
    return get_scores()


@data_blueprint.route("/scores", methods=["POST"])
def update_data_in_file():
    score_data = request.get_json()["result"]
    log_data = request.get_json()["log"]
    add_score(score_data)
    add_log(log_data)
    return "OK"


@data_blueprint.route("/empty-scores", methods=["POST"])
def empty_scores_file():
    empty_scores()
    return "OK"


@data_blueprint.route("/empty-logs", methods=["POST"])
def empty_log_file():
    empty_log()
    return "OK"


@data_blueprint.route("/logs", methods=["GET"])
def get_log_file():
    return get_logs()