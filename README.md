# Bank Data ETL Project (AWS Free Tier)

# Project Components & Step-by-Step Implementation

## 1. Data Ingestion (Upload Raw Data to S3)

- **Create an S3 bucket** (e.g., bank-raw-data-bucket).
- **Upload raw CSV files** containing bank prospect data manually or using AWS CLI.
- **The raw data** contains customer demographics, transaction, and marketing info.

## 2. Data Cataloging (AWS Glue Crawler)

- **Create a Glue Crawler** (BankRawDataCrawler) pointing to the raw data S3 path.
- **Run crawler** to automatically infer schema and populate Glue Data Catalog.
- **Crawler can be scheduled** or run on demand.

## 3. ETL Job Automation (AWS Lambda Trigger)

- **Configure S3 event notifications** for PUT (object created) events on raw data bucket.
- **Create a Lambda function** that triggers the Glue ETL job when new data arrives.
- **Lambda uses AWS SDK (boto3)** to start Glue jobs programmatically.

## 4. Data Transformation (AWS Glue ETL Job with Spark)

- **Create a Glue ETL job** (BankDataTransformationJob) using PySpark.
- **Read raw CSV data** from S3.
- **Clean data:** remove duplicates, handle missing values.
- **Enrich data:** derive new columns like age groups.
- **Write transformed data** back to S3 curated bucket in partitioned Parquet format.

## 5. Data Storage (Curated S3 Bucket)

- **Create a separate S3 bucket** (e.g., bank-curated-data-bucket).
- **Store transformed data** in optimized parquet format.
- **Partition data** by meaningful fields (e.g., age_group) for query performance.

## 6. Data Querying (AWS Athena)

- **Create Athena database** and external tables referencing the curated S3 bucket.
- **Use Athena SQL** to query transformed data directly without data movement.
- **Run MSCK REPAIR TABLE** to sync partitions after each data update.

## 7. Monitoring & Logging (AWS CloudWatch)

- **Enable Glue job and Lambda function logs** to CloudWatch.
- **Monitor job runs, execution time, errors.**
- **Configure CloudWatch alarms** for job failures or anomalies.

---

# How the Pipeline Works (End-to-End Flow)

**Upload raw data CSV to S3 raw bucket →  
S3 event triggers Lambda function →  
Lambda function starts Glue ETL job →  
Glue crawler updates schema catalog (if needed) →  
Glue job runs Spark script to clean and enrich data →  
Transformed data saved as Parquet files in S3 curated bucket →  
Athena tables updated and available for SQL queries →  
CloudWatch monitors and logs all jobs and functions.**

---

# Benefits & Highlights

- **Automation:** Fully event-driven pipeline with zero manual intervention after initial setup.
- **Scalability:** Spark cluster handles large datasets in parallel.
- **Cost-Efficiency:** Serverless AWS services minimize infrastructure overhead.
- **Performance:** Parquet storage and partitioning optimize query speeds in Athena.
- **Reliability:** Monitoring with CloudWatch ensures fast troubleshooting.


## Overview
This project builds a complete ETL pipeline for bank prospect data using AWS services:
- **S3**: Stores raw and processed CSV data
- **Glue**: ETL job using Spark for data cleaning and enrichment
- **Lambda**: Triggers Glue job
- **Athena**: Runs SQL queries on processed S3 data
- **CloudWatch**: Logs and monitors job runs

## Glue Script
Performs:
- Cleaning null values
- Converting names to uppercase
- Categorizing customers by credit score and loan amount

## Athena Table
Queries data using SQL directly from S3.

## Lambda Function
Triggers the Glue ETL job.




![Image Alt](https://github.com/suma419/ETL-Bank-Transformation-Project/blob/fca23dbaf2267b3e23806ad21126de88859269b0/bankprospects_ETL_Glue_job_output_csv_file.png)]
