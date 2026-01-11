import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue Context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ================================
# INPUT & OUTPUT PATHS
# ================================
input_path = "s3://youtube-transformed-anu/processed_data/"
output_path = "s3://youtube-transformed-anu/parquet_data/"

# ================================
# READ JSON DATA FROM S3
# ================================
df = spark.read.json(input_path)

print("Schema of input data:")
df.printSchema()

print("Sample records:")
df.show(5, truncate=False)

# ================================
# WRITE DATA AS PARQUET
# ================================
df.write \
    .mode("overwrite") \
    .parquet(output_path)

print("Parquet files written successfully to:", output_path)

job.commit()
