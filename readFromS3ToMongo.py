#import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from dotenv import load_dotenv
import os


#load environment variables
load_dotenv()
#read from s3 bucket
mongo_uri = os.getenv("MONGODB_URI")
accesskey = os.getenv("AWS_ACCESS_KEY")
secretkey = os.getenv("AWS_SECRET_KEY")
s3_bucket_resource = os.getenv("S3_BUCKET_RESOURCE")


spark = SparkSession.builder\
    .appName("myapp")\
    .config("spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.3.4,"
            "org.apache.hadoop:hadoop-common:3.3.4,"
            "org.apache.hadoop:hadoop-client-api:3.3.6,"
            "org.apache.hadoop:hadoop-client-runtime:3.3.6,"
            "com.amazonaws:aws-java-sdk-bundle:1.12.262,"
            "org.mongodb.spark:mongo-spark-connector_2.12:10.4.0,"
            "org.mongodb:mongodb-driver-sync:4.10.2,"
            "org.mongodb:mongodb-driver-core:4.10.2,"
            "org.mongodb:bson:4.10.2") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.mongodb.read.connection.uri", mongo_uri)\
    .config("spark.mongodb.write.connection.uri", mongo_uri)\
    .config("spark.mongodb.write.convertJson","any")\
    .config("spark.hadoop.fs.s3a.access.key", accesskey) \
    .config("spark.hadoop.fs.s3a.secret.key", secretkey) \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .getOrCreate()

#read parquet
df = spark.read.parquet(s3_bucket_resource)
df.show()

#transform data
df = df.withColumn("priceSqrtMeter", df["price"]/df["area"])

#write to mongodb
df.write.format("mongodb").option("database","spark").option("collection", "readfroms3").mode("append").save()

#print progress
print("Data written to MongoDB")


