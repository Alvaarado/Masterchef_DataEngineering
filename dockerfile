# Usa una imagen base de Python

FROM python:3.12.4

# Configura el directorio de trabajo

WORKDIR /app

# Copia el archivo de requisitos y el código de la aplicación al contenedor

COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias

RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto que la aplicación utilizará

EXPOSE 8000

# Ejecuta la aplicación FastAPI usando uvicorn

CMD ["uvicorn", "app_recetas:app", "--host", "0.0.0.0", "--port", "8000"]
