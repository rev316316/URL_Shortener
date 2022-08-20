from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy
DB_NAME =  'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '316316316'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .URL_Shortener import us

    app.register_blueprint(us, url_prefix="/")

    from .models import placeholder

    return app


def create_database(app):
    if not path('URL-Shortener/' + DB_Name):
        db.create_all(app=app)
        print('Created Database!')
