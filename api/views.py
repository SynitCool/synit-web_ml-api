from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html")

@views.route("/home")
def home():
    return render_template("home_pages/home.html")

@views.route("/api")
def api():
    return render_template("api_pages/api_overview.html")

@views.route("/about")
def about():
    return render_template("about_pages/about.html")

@views.route("/scrt-pgs/none-ks/jt-df-rm/dly")
def secret():
    return "<p>01101001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101 00100000 01100010 01100001 01100010 01100101 <p><p>愛してます<p>"