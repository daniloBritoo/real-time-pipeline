from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp, from_unixtime
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("SensorStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0")\
    .getOrCreate()

schema = StructType([
        StructField("sensor_id", IntegerType()),
        StructField("timestamp", DoubleType()),
        StructField("temperature", DoubleType())
])

df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "temperature_sensor")\
        .option("maxOffsetsPerTrigger", 10)\
        .load()
        
df = df.selectExpr("CAST(value AS STRING) as json") \
       .select(from_json(col("json"), schema).alias("data")) \
       .select("data.*") \
       .withColumn("timestamp", to_timestamp(from_unixtime("timestamp")))
       
       
query = df.writeStream \
    .format("csv") \
    .option("path", "streaming_insert") \
    .option("checkpointLocation", "checkpoint/") \
    .outputMode("append") \
    .trigger(processingTime='10 seconds') \
    .start()


try:
    query.awaitTermination()
except KeyboardInterrupt:
    print("Streaming interrompido")
    query.stop()
    spark.stop()