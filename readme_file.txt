# 🏦 Bank Data Transform Pipeline (AWS Free Tier)

## 📌 Project Overview
This project builds a scalable and serverless ETL pipeline using AWS services to process over 1 million bank prospect records. It includes raw data ingestion, transformation using PySpark, automation with Lambda, SQL-based analytics with Athena, and logging via CloudWatch — all inside the AWS Free Tier.

---

## 🧱 Architecture Flow (with Stages)

1. **📥 Upload Raw Data to Amazon S3**
   - Store input CSV file (`bank_prospect_data.csv`) in the `s3://bank-prospects/raw/` folder.

2. **🧠 Run AWS Glue Crawler**
   - Automatically scans and infers the schema from raw CSV.
   - Creates a catalog table (e.g., `bank_data_db.raw`) to make data queryable.

3. **⚙️ Develop & Run AWS Glue ETL Job (Spark)**
   - Written in Python (PySpark).
   - Cleans missing records, transforms names to uppercase.
   - Adds a new `risk_category` column based on credit score and loan amount.
   - Writes output to `s3://bank-prospects/processed/`.

4. **🧾 Create Athena Table Over Processed Data**
   - Points to `processed/` folder.
   - Enables direct SQL queries on enriched customer data.

5. **📊 Query with Athena**
   - Run SQL to analyze:
     - High-risk customer segments
     - Loan behavior by age/income
     - Credit distribution and fraud risk

6. **⏱️ (Optional) Automate ETL with AWS Lambda**
   - Lambda triggers Glue job when a new file is added.
   - Fully serverless and event-driven.

7. **📉 Monitor with AWS CloudWatch**
   - Track Glue job execution logs.
   - Debug schema mismatches or job failures.
   - Set alerts if needed.

---

## 📂 Files Included

| File                          | Description                                     |
|-------------------------------|-------------------------------------------------|
| `etl_glue_script.py`          | Glue job script for transformation (PySpark)   |
| `lambda_trigger_glue.py`      | Lambda function to trigger Glue job            |
| `athena_create_table.sql`     | SQL to define external Athena table            |
| `README.md`                   | This documentation                            |
| `bank_etl_flowchart.png`      | Visual representation of full ETL pipeline     |

---

## 🔄 How This All Connects

```text
S3 (raw CSV)
   ↓
Glue Crawler → Catalog Table
   ↓
Glue ETL Job → Clean, Transform → Save to S3 (processed/)
   ↓
Athena Table (on processed/)
   ↓
SQL Queries (Insights)
   ↓
(Optional) Lambda → Auto-trigger ETL
   ↓
CloudWatch → Logs & Monitoring
🧠 Built Using:
Amazon S3

AWS Glue (Crawler + Job)

AWS Lambda

AWS Athena

AWS CloudWatch

Python (PySpark)

💸 AWS Free Tier Budget
All services used (10 DPUs/month for Glue, 5 GB S3, 1 million Athena queries/month) are within Free Tier limits.

yaml
Copy
Edit

---

## 🖼️ Flowchart: Visual Pipeline Representation

🔗 Download image: [**bank_etl_flowchart.png**](sandbox:/mnt/data/bank_data_etl_complete.zip)

And here’s what it looks like conceptually:

```text
⬢ Upload raw CSV to S3 (raw/)
   ↓
⬢ Run AWS Glue Crawler → Create Data Catalog Table
   ↓
⬢ Develop and Run Glue ETL Job (Spark, Python)
      ↳ Clean nulls
      ↳ Uppercase names
      ↳ Add 'risk_category'
   ↓
⬢ Store processed CSV to S3 (processed/)
   ↓
⬢ Use Athena to create SQL table over processed data
   ↓
⬢ Run analytical SQL queries (e.g., risk analysis)
   ↓
⬢ (Optional) Automate ETL with AWS Lambda
   ↓
⬢ Monitor Glue logs using CloudWatch