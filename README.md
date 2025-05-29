# Bank Data ETL Project (AWS Free Tier)

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
