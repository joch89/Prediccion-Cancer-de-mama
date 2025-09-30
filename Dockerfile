# Usa una imagen base de Python
FROM python:3.10-slim

# Establecer carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements.txt primero y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo lo demás a /app
COPY . .

# Exponer el puerto 5000 (el que usa Flask)
EXPOSE 5000

# Comando por defecto para ejecutar la API Flask
CMD ["python", "app.py"]
