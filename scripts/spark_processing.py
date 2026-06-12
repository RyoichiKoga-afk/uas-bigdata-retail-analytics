import os
import pandas as pd

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("RetailVisitorAnalytics") \
    .getOrCreate()

# ==========================
# Baca data
# ==========================

df = spark.read.csv(
    r"C:\uas-tbg\data\visitor_data.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "timestamp",
    to_timestamp("timestamp")
)

# ==========================
# Total visitor per zone
# ==========================

visitor_total = df.groupBy("zone").agg(
    sum("visitor_count").alias("total_visitors")
)

visitor_total_pd = visitor_total.toPandas()

os.makedirs(
    r"C:\uas-tbg\output\visitor_total",
    exist_ok=True
)

visitor_total_pd.to_parquet(
    r"C:\uas-tbg\output\visitor_total\visitor_total.parquet",
    index=False
)

# ==========================
# Visitor trend per 15 menit
# ==========================

visitor_time = (
    df.withColumn(
        "time_block",
        floor(minute("timestamp") / 15)
    )
    .groupBy("zone", "time_block")
    .agg(
        avg("visitor_count").alias("avg_visitors")
    )
)

visitor_time_pd = visitor_time.toPandas()

os.makedirs(
    r"C:\uas-tbg\output\visitor_time",
    exist_ok=True
)

visitor_time_pd.to_parquet(
    r"C:\uas-tbg\output\visitor_time\visitor_time.parquet",
    index=False
)

# ==========================
# Dataset ML
# ==========================

ml_dataset = (
    df.withColumn(
        "hour",
        hour("timestamp")
    )
    .select(
        "hour",
        "visitor_count",
        "zone"
    )
)

ml_dataset_pd = ml_dataset.toPandas()

os.makedirs(
    r"C:\uas-tbg\output\ml_visitor",
    exist_ok=True
)

ml_dataset_pd.to_parquet(
    r"C:\uas-tbg\output\ml_visitor\ml_visitor.parquet",
    index=False
)

print("Parquet berhasil dibuat")

spark.stop()