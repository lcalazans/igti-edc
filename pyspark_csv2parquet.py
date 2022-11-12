from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("PracticalWork")
    .getOrCreate()
)

# ler dados do enem 2020
enem = (
    spark
    .read
    .format('csv')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', ';')
    .load('s3://datalake-leonardo-igti/data_raw/DADOS/')
)

(
    enem
    .write
    .mode('overwrite')
    .format('parquet')
    .save('s3://datalake-leonardo-igti/consumer-zone/enem/')
)
