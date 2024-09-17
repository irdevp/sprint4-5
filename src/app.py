from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Função para carregar o modelo do disco
def local_model():
    try:
        local_model_path = 'models/random_forest_model.pkl'
        model = joblib.load(local_model_path)
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None

# Carregue o modelo uma vez na inicialização do servidor
model = local_model()

# Inicialize os codificadores de rótulos com todas as categorias esperadas
meal_plan_encoder = LabelEncoder().fit(["Meal Plan 1", "Meal Plan 2", "Not Selected"])
room_type_encoder = LabelEncoder().fit(["Room_Type 1", "Room_Type 2", "Room_Type 3", "Room_Type 4", "Room_Type 5", "Room_Type 6"])
market_segment_encoder = LabelEncoder().fit(["Online", "Offline", "Corporate"])
booking_status_encoder = LabelEncoder().fit(["Not_Canceled", "Canceled"])

@app.route('/api/v1/inference', methods=['POST'])
def infer():
    try:
        data = request.json

        # Codificar as variáveis categóricas com verificação de categorias desconhecidas
        try:
            type_of_meal_plan = meal_plan_encoder.transform([data['type_of_meal_plan']])[0]
        except ValueError:
            return jsonify({"error": f"Unknown meal plan: {data['type_of_meal_plan']}"}), 400
        
        try:
            room_type_reserved = room_type_encoder.transform([data['room_type_reserved']])[0]
        except ValueError:
            return jsonify({"error": f"Unknown room type: {data['room_type_reserved']}"}), 400
        
        try:
            market_segment_type = market_segment_encoder.transform([data['market_segment_type']])[0]
        except ValueError:
            return jsonify({"error": f"Unknown market segment: {data['market_segment_type']}"}), 400
        
        try:
            booking_status = booking_status_encoder.transform([data['booking_status']])[0]
        except ValueError:
            return jsonify({"error": f"Unknown booking status: {data['booking_status']}"}), 400

        # Crie um DataFrame com os dados recebidos e os nomes das características
        feature_names = [
            'no_of_adults', 'no_of_children', 'no_of_weekend_nights', 'no_of_week_nights',
            'type_of_meal_plan', 'required_car_parking_space', 'room_type_reserved', 
            'lead_time', 'arrival_year', 'arrival_month', 'arrival_date', 
            'market_segment_type', 'repeated_guest', 'no_of_previous_cancellations', 
            'no_of_previous_bookings_not_canceled', 'no_of_special_requests', 'booking_status'
        ]

        features = pd.DataFrame([[
            data['no_of_adults'],
            data['no_of_children'],
            data['no_of_weekend_nights'],
            data['no_of_week_nights'],
            type_of_meal_plan,
            data['required_car_parking_space'],
            room_type_reserved,
            data['lead_time'],
            data['arrival_year'],
            data['arrival_month'],
            data['arrival_date'],
            market_segment_type,
            data['repeated_guest'],
            data['no_of_previous_cancellations'],
            data['no_of_previous_bookings_not_canceled'],
            data['no_of_special_requests'],
            booking_status
        ]], columns=feature_names)

        # Diagnóstico: Imprimir as características recebidas
        print(f"Features: {features}")

        # Diagnóstico: Verificar as características esperadas pelo modelo
        if hasattr(model, 'feature_names_in_'):
            print(f"Expected features: {model.feature_names_in_}")

        # Realize a inferência
        prediction = model.predict(features)[0]
        return jsonify({'result': int(prediction)}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def read_root():
    return {"message": "API is running"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
