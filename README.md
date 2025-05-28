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

All components are within AWS Free Tier usage.
