from flask import Flask

def create_app():
    app = Flask(__name__)
    from .URL_Shortener import us
    app.register_blueprint(us, url_prefix="/")
    return app
