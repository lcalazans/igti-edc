resource "aws_s3_bucket" "datalake" {
    # parâmetros de configuração do recurso do projeto 
    bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
    acl = "private"

    server_side_encryption_configuration {
        rule {
          apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
          }
        }
    }

    tags = {
        IES = "IGTI"
        CURSO = "EDC"
    }
  
}

resource "aws_s3_bucket_object" "codigo_spark" {
    bucket = aws_s3_bucket.datalake.id
    key = "emr-code/pyspark/job_spark_from_tf.py"
    acl = "private"
    source = "../pyspark_csv2parquet.py"
    etag = filemd5("../pyspark_csv2parquet.py")
  
}

provider "aws" {
  region = "us-east-2"
}