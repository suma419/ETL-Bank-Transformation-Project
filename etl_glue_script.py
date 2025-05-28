import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import col, when, upper

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw data
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="bank_data_db",
    table_name="raw"
)

# Clean and transform
df = datasource.toDF()
df_clean = df.dropna(subset=["customer_id", "first_name", "last_name", "email", "credit_score", "loan_amount"])
df_upper = df_clean.withColumn("first_name", upper(col("first_name"))).withColumn("last_name", upper(col("last_name")))
df_risk = df_upper.withColumn(
    "risk_category",
    when((col("credit_score") < 600) | (col("loan_amount") > 50000), "High")
    .when((col("credit_score") >= 600) & (col("credit_score") <= 700), "Medium")
    .otherwise("Low")
)

# Convert back and write
final_dynamic_df = DynamicFrame.fromDF(df_risk, glueContext, "final_dynamic_df")
glueContext.write_dynamic_frame.from_options(
    frame=final_dynamic_df,
    connection_type="s3",
    connection_options={"path": "s3://bank-prospects/processed/"},
    format="csv",
    format_options={"withHeader": True}
)

job.commit()
