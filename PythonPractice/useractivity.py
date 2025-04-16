from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date
from pyspark.sql.types import StructType, StructField, StringType, DateType

spark = SparkSession.builder.getOrCreate()

# Sample data
data = [
    ("u1", "Alice", "open", "US", "2025-04-01"),
    ("u2", "Bob", "closed", "US", "2025-04-03"),
    ("u3", "Charlie", "open", "US", "2025-04-05"),
    ("u4", "David", "open", "US", "2025-04-06"),
    ("u5", "Eve", "open", "US", "2025-04-07")
]

# Define schema
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("status", StringType(), True),
    StructField("country", StringType(), True),
    StructField("last_active_date", StringType(), True),
])

df = spark.createDataFrame(data, schema)

# Convert last_active_date to DateType
df = df.withColumn("last_active_date", to_date("last_active_date", "yyyy-MM-dd"))

# Filter US users only
df_us = df.filter(df.country == "US")

df_us.show(truncate=False)

#distinct last_active_date
dates_df = df_us.select("last_active_date").distinct().withColumnRenamed("last_active_date", "date")


# Create a date range for the last 7 days including the last active date
from pyspark.sql import functions as F

user_date_df = df_us.alias("u").crossJoin(dates_df.alias("d")).filter(
    (F.col("u.last_active_date") <= F.col("d.date")) &
    (F.col("u.last_active_date") >= F.expr("date_sub(d.date, 6)"))
)
user_date_df.show(truncate=False)

# Add is_active column
user_date_df = user_date_df.withColumn(
    "is_active", F.when(F.col("u.status") == "open", 1).otherwise(0)
).select("d.date", "u.user_id", "is_active").dropDuplicates(["date", "user_id"])

user_date_df.show()

#rolling stats
rolling_stats = user_date_df.groupBy("date").agg(
    F.count("user_id").alias("total_users"),
    F.sum("is_active").alias("active_users")
).withColumn(
    "active_user_share", F.round((F.col("active_users") / F.col("total_users")) * 100, 2)
)

rolling_stats.orderBy("date").show()