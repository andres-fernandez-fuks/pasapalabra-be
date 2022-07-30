from project import db


class Score(db.Model):
    __tablename__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    correct_answers = db.Column(db.SmallInteger)
    incorrect_answers = db.Column(db.SmallInteger)
    remaining_time = db.Column(db.SmallInteger)
    user_name = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, correct_answers, incorrect_answers, remaining_time, user_name):
        self.correct_answers = correct_answers
        self.incorrect_answers = incorrect_answers
        self.remaining_time = remaining_time
        self.user_name = user_name
