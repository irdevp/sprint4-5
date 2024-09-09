from flask import Blueprint, jsonify
from sqlmodel import Session, select
from models.carro import Carro
from core.db import engine

hotelRouter = Blueprint("carros", __name__)

@hotelRouter.route('/', methods=['GET'])
def get_carros():
    try:
        with Session(engine) as session:
            statement = select(Carro)  
            carros = session.exec(statement).all()
            return jsonify([carro.dict() for carro in carros]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
