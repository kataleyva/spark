#1. Llamar imagen base del proyecto
FROM python:3.9-slim

#2. Definir directorio de trabajo dentro del contenefot o fumas
WORKDIR /app

#2.5 Spark para funcionar necesita java
RUN apt-get update && apt-get install -y default -jre

#3. Copiar el archivo de requerimientos y se instalan dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

#4. Copiar todos los archivos 
COPY . . 

#5. Ejecutar comando para ejecutar app
CMD ["python", "app.py",]
