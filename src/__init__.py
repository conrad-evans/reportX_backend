from flask import Flask
from src.views.auth import auth_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_blueprint)

    return app
