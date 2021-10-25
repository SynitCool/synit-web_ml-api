from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return "<h1>This is index</h1>"

@views.route("/home")
def home():
    return "<h1>This is Home</h1>"