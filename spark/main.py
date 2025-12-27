from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("DorisPySparkExample") \
    .getOrCreate()

df = spark.read \
    .format("doris") \
    .option("doris.table.identifier", "MyDB.example_unique_table") \
    .option("doris.fenodes", "172.28.0.10:8030") \
    .option("user", "root") \
    .option("password", "") \
    .load()

df.show() 

