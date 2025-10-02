# API de Predicción Breast Cancer

Este proyecto contiene un **modelo de Machine Learning** entrenado con el dataset Breast Cancer (Wisconsin) y una **API REST con Flask** para realizar predicciones. Además, el proyecto está **dockerizado** y cuenta con un workflow de **CI/CD en GitHub Actions** que construye, prueba y publica la imagen en Docker Hub automáticamente.

---

## 1. Descripción del proyecto

- **Modelo Predictivo:** Random Forest entrenado con el dataset Breast Cancer de sklearn.
- **API:**  
  - `GET /` → prueba el estado del servicio  
  - `POST /predict` → recibe un JSON con 30 características y devuelve la predicción (benigno/maligno)
- **Docker:** Contenedor con API y modelo listo para ejecutar en cualquier máquina con Docker.
- **CI/CD:** Workflow en GitHub Actions que construye, prueba y publica la imagen.

---

## 2. Requisitos

- Python 3.10+
- Docker Desktop
- Git
- (Opcional) PowerShell o terminal Bash para pruebas

---

## 3. Clonar el repositorio

```bash
git clone https://github.com/joch89/Prediccion-Cancer-de-mama.git
cd Prediccion-Cancer-de-mama
```

## 4. Ejecutar la API localmente (sin Docker)

```bash
python app.py
```
La API quedará disponible en http://localhost:5000

## 5. Probar la API
El repositorio ya incluye un archivo `entrada.json` con un ejemplo de entrada válido.

Opción 1: Usando `curl` (Linux / macOS / Git Bash en Windows)
```bash
curl -X POST -H "Content-Type: application/json" \
-d @entrada.json \
http://localhost:5000/predict
```

Opción 2: Usando PowerShell (Windows)
```bash
Invoke-RestMethod -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body (Get-Content .\entrada.json -Raw)
```

Ejemplo de salida esperada
![Resultado esperado](images/imagen1.png)

Usando curl (Linux/macOS o PowerShell con curl):
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"features": [17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.905,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]}' \
http://localhost:5000/predict
```
Usando PowerShell:

```bash
Invoke-RestMethod -Uri http://localhost:5000/predict `
  -Method POST `
  -ContentType "application/json" `
  -Body (Get-Content .\entrada.json -Raw)
```
Respuesta esperada:

```bash
{"prediction": 1}
```

## 6. Ejecutar con Docker
1. Construir la imagen:
```bash
docker build -t breast_api .
```
2. Correr el contenedor:
```bash
docker run -d -p 5000:5000 --name breast_api breast_api
```
3. Probar la API en http://localhost:5000/predict usando los comandos de curl o PowerShell mencionados antes.
4. Detener el contenedor:
```bash
docker stop breast_api
docker rm breast_api
```

## 7. CI/CD (GitHub Actions)

El workflow CI/CD Breast Cancer API hace lo siguiente automáticamente cuando haces push al branch main:

1. Construye la imagen Docker de la API.
2. Levanta un contenedor temporal y prueba el endpoint /predict.
3. Hace login en Docker Hub y publica la imagen (<tu_usuario_docker>/breast_api:latest).

Esto permite tener siempre la última versión de la API disponible para cualquier máquina sin necesidad de ejecutar pasos manuales.

