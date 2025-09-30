# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo entrenado
model = joblib.load("modelo.pkl")

@app.route("/")
def home():
    return "Bienvenido a mi API ML con Flask y Docker (Breast Cancer)"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # JSON con datos
    # El JSON debe tener un campo 'features' con la lista de valores
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
