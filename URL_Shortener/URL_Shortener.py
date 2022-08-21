from flask import Flask, redirect, Blueprint
import hashlib

url_dict = {"randombullshit": "google.com"}

us = Blueprint('us', __name__)

app = Flask(__name__)

def url_shortner(url):
    url_short = hashlib.md5(url.encode()).hexdigest()[:7]
    return url_short


@us.route('/create/<path:longurl>', methods=["POST"])
def create_short_url(longurl):
    short_url = url_shortner(longurl)  # sd1as23d1
    url_dict[short_url] = longurl  # url_dict = { sd1asadasd: longurl }
    return f"http://127.0.0.1:5000/{short_url}"


@us.route('/<shorturl>')
def get_redirected(shorturl):
    return redirect(url_dict[shorturl])


@us.route('/home')
def index():
    return "Hello Human Being"


