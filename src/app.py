from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify(message="API Grupo 5")

# Rota de inferência
@app.route('/api/inference', methods=['POST'])
def inference():
    data = request.json
    return jsonify(message="Inference", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
