from . import db


class placeholder(db.model):
    id = db.Column(db.integer, primary_key=True)
    long_url = db.Column(db.string(150), unique=True)
    short_url = db.Column(db.string(150), unique = True)


