from flask import Blueprint, jsonify,request
from sqlmodel import Session, select
from models.hotelModel import Reserva
from core.db import engine

import joblib
import pandas as pd
import boto3
import os

# Configurações do S3
s3_bucket ='hotelreservationsgrupo5'
s3_key = 'random_forest_model.pkl'
local_model_path = './local_model.pkl'

hotelRouter = Blueprint("hotel", __name__)

# Verificar se o diretório local existe e criar se necessário
os.makedirs(os.path.dirname(local_model_path), exist_ok=True)

# Baixar o modelo do S3
s3_client = boto3.client('s3')
s3_client.download_file(s3_bucket, s3_key, local_model_path)

# Carregar o modelo treinado
model = joblib.load(local_model_path)

    

@hotelRouter.route('/', methods=['POST'])
def inference():
    if model is None:
        return jsonify({'error': 'Modelo não carregado'}), 500

    data = request.json
    features = [data['no_of_adults'], data['no_of_children'], data['type_of_meal_plan']]
    prediction = model.predict([features])
    return jsonify({'result': int(prediction[0])})