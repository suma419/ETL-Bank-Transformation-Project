-- Athena Table Creation SQL
CREATE EXTERNAL TABLE IF NOT EXISTS bank_data_db.processed_data (
  customer_id STRING,
  first_name STRING,
  last_name STRING,
  email STRING,
  age INT,
  gender STRING,
  annual_income DOUBLE,
  credit_score INT,
  account_balance DOUBLE,
  loan_amount DOUBLE,
  loan_status STRING,
  risk_category STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar" = "\"",
  "escapeChar" = "\\"
)
LOCATION 's3://bank-prospects/processed/'
TBLPROPERTIES ('skip.header.line.count'='1');
