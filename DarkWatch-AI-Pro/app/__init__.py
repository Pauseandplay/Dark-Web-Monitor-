from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="change-this-secret-key",
        APP_NAME="DarkWatch AI"
    )
    app.register_blueprint(main)
    return app
