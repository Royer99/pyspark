# PySpark Data Processing with S3 and MongoDB

## Overview
This script utilizes **PySpark** to read a Parquet file from an **Amazon S3** bucket, perform a simple transformation on the data, and write the processed data to **MongoDB**.

## Prerequisites
Ensure you have the following installed and configured:

- Python 3.x
- Apache Spark 3.5.5
- Hadoop AWS libraries
- MongoDB Spark Connector
- AWS S3 credentials
- `.env` file containing environment variables

## Dependencies
The script relies on the following Python libraries:

```python
pyspark
python-dotenv
```

## Environment Variables
The script loads required environment variables from a `.env` file. Ensure this file contains the following keys:

```
MONGODB_URI=<your_mongodb_connection_uri>
AWS_ACCESS_KEY=<your_aws_access_key>
AWS_SECRET_KEY=<your_aws_secret_key>
S3_BUCKET_RESOURCE=<s3_bucket_path>
```

## Installation
Create and activate a new venv
```bash
python3 -m venv myenv
source myenv/bin/activate
```

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Configuration
The script initializes a **SparkSession** with the necessary configurations for:
- Connecting to AWS S3 using Hadoop's S3A file system.
- Connecting to MongoDB for reading and writing.
- Specifying required Spark and Hadoop dependencies.

## Usage
Run the script using:

```bash
python readFromS3ToMongo.py
```

## Workflow
1. **Load Environment Variables**: Reads MongoDB URI and AWS credentials.
2. **Initialize Spark Session**: Configures dependencies and sets up connections.
3. **Read Data from S3**: Loads a Parquet file into a PySpark DataFrame.
4. **Transform Data**: Computes the `priceSqrtMeter` column by dividing `price` by `area`.
5. **Write to MongoDB**: Stores the processed data in MongoDB under the `spark.readfroms3` collection.
6. **Prints Confirmation**: Logs success message upon completion.

## Spark Dependencies
The script includes the following dependencies in the Spark session:
- `hadoop-aws:3.3.4`
- `aws-java-sdk-bundle:1.12.262`
- `mongo-spark-connector_2.12:10.4.0`
- `mongodb-driver-sync:4.10.2`
- `mongodb-driver-core:4.10.2`
- `bson:4.10.2`

## Notes
- Ensure your **AWS credentials** and **MongoDB URI** are correctly configured.
- The script uses **append mode** when writing to MongoDB.
- Make sure the S3 bucket contains the required Parquet file before executing the script.


---
**Author:** Royer Arenas  
**Date:** 2025-03-11

