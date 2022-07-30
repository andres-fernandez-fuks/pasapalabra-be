from project import db

class Log(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=False, nullable=True)
    log_message = db.Column(db.String(1000), unique=False, nullable=False)

    def __init__(self, user_name, log_message):
        self.user_name = user_name
        self.log_message = log_message