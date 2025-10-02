
## Materia: Automatizacion de Infraestructura II
## Profesor
## Alumno: Marvin Israel Jaramillo Garcia
# Usa la imagen oficial de Python en versión ligera (slim)
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia e instala dependencias. Usamos --no-cache-dir para un menor tamaño de imagen
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# El puerto que escuchará Flask
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]