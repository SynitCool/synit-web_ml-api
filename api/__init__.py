from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "the_secret_key_is_cool"

    from .views import views
    from .online_shopper_views import online_shopper_views
    from .online_shopper.online_shopper_api import online_shopper_api

    app.register_blueprint(views)
    app.register_blueprint(online_shopper_views)
    app.register_blueprint(online_shopper_api)

    return app
