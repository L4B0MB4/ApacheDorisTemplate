from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("DorisPySparkExample") \
    .config("spark.driver.extraClassPath", "./jars/spark-doris-connector-spark-3.5-25.2.0.jar") \
    .getOrCreate()

df = spark.read \
    .format("doris") \
    .option("doris.table.identifier", "MyDB.example_unique_table") \
    .option("doris.fenodes", "172.28.0.10:8030") \
    .option("user", "root") \
    .option("password", "") \
    .load()

df.show() 

spark.stop()