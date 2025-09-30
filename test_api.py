import requests

# URL del endpoint
url = "http://127.0.0.1:5000/predict"

# Datos de entrada (30 valores)
data = {
    "features": [
        17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.0787,
        1.095, 0.9053, 8.589, 153.4, 0.0064, 0.049, 0.0537, 0.0159, 0.03, 0.0062,
        25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189
    ]
}

# Enviar solicitud POST
try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Lanza error si el status no es 200
    resultado = response.json()
    print("✅ Predicción recibida:", resultado)
except requests.exceptions.RequestException as e:
    print("❌ Error al conectar con la API:", e)