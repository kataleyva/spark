from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# 1. Crear la sesión de Spark
# Nos conectamos al maestro de Spark que Docker Compose creará.
# El nombre 'spark-master' es el nombre del servicio en docker-compose.yml
spark = SparkSession.builder \
    .appName("MiPrimeraAppSpark") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# 2. Cargar los datos
# La ruta '/app/data.csv' es la ruta DENTRO del contenedor
df = spark.read.csv("/app/data.csv", header=True, inferSchema=True)

# 3. Realizar una transformación de Big Data (agregación)
print("Calculando el total de ventas por categoría...")
ventas_por_categoria = df.groupBy("categoria").agg(sum("ventas").alias("ventas_totales"))

# 4. Mostrar el resultado
ventas_por_categoria.show()

# 5. Detener la sesión de Spark
spark.stop()