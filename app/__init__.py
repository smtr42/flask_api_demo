
from flask import Flask
from app.api.api import version_1_blueprint



def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(version_1_blueprint)
    return flask_app