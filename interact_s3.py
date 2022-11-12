import boto3
import pandas as pd

# definições
bucket = 'datalake-leonardo-igti'
data = 'data_raw/DADOS/MICRODADOS_ENEM_2020.csv'

# criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.upload_file(data, bucket, data)
