from flask import Flask
from core.db import engine
from models import create_db_and_tables
from core.config import Config

def initialize_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    create_db_and_tables()

    # Registro de blueprints de rotas
    from api.v1.endpoints.hotelEnpoints import hotelRouter
    app.register_blueprint(hotelRouter, url_prefix="/api/v1/inference")


    return app
