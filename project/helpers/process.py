import io
from project.models.log import Log
from project.models.score import Score
from project import db
from flask import jsonify


def add_score(new_score):
    score = Score(
        user_name=new_score[0],
        correct_answers=int(new_score[1]),
        incorrect_answers=int(new_score[2]),
        remaining_time=int(new_score[3]),
    )
    db.session.add(score)
    db.session.commit()
    return score


def add_log(log_data):
    log_string = ""
    for key in log_data[1]:
        if key == "playerName":
            continue
        log_string += f"{key}: {log_data[1][key]}\n"
    log = Log(user_name=log_data[0], log_message=log_string)
    db.session.add(log)
    db.session.commit()
    return log


def empty_scores():
    db.engine.execute("""TRUNCATE TABLE scores""")


def empty_log():
    db.engine.execute("""TRUNCATE TABLE logs""")


def get_logs():
    logs = Log.query.all()[:20]
    log_info = ""
    for log in logs:
        log_info += f"{log.user_name}: {log.log_message}\n"

    return log_info


def get_scores():
    scores = Score.query.distinct(Score.user_name).all()
    sorted_scores = sorted(
        scores,
        key=lambda x: (-x.correct_answers, x.incorrect_answers, -x.remaining_time),
    )
    return jsonify(
        [
            [
                score.user_name,
                score.correct_answers,
                score.incorrect_answers,
                score.remaining_time,
            ]
            for score in sorted_scores[:20]
        ]
    )
