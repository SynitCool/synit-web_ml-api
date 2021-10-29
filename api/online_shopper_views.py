from flask import Blueprint, render_template

online_shopper_views = Blueprint("online_shopper_views", __name__)

@online_shopper_views.route("/api/online-shopper/overview")
def online_shopper_overview():
    return render_template("api_pages/online_shopper/online_shopper_overview.html")

@online_shopper_views.route("/api/online-shopper/feature")
def online_shopper_feature():
    return render_template("api_pages/online_shopper/online_shopper_feature.html")

@online_shopper_views.route("/api/online-shopper/credit")
def online_shopper_credit():
    return render_template("api_pages/online_shopper/online_shopper_credit.html")