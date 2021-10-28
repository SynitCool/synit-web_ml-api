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
    return render_template("api_pages/api.html")

@views.route("/about")
def about():
    return render_template("about_pages/about.html")
