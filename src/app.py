from flask import Flask
from core.db import engine
from core.config import Config
from api.v1.endpoints.hotelEnpoints import hotelRouter

def initialize_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(hotelRouter, url_prefix="/api/v1/hotel")

    return app


if __name__ == "__main__":

    app = initialize_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
