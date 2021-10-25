from flask import Blueprint

online_shopper_api = Blueprint("online_shopper_api", __name__)

@online_shopper_api.route("/online_shopper_api", methods=["POST"])
def online_shopper_model():
    return "<h1>Online Shopper API</h1>"