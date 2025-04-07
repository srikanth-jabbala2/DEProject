from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from sqlalchemy import create_engine
import pandas as pd
import pyodbc
import os

#connect to sql server
server = 'localhost'
database = 'sqlpractice'
driver = 'ODBC Driver 17 for SQL Server'
Trusted_Connection='yes'
connection_string = f"mssql+pyodbc://{server}/{database}?driver={driver.replace(' ', '+')}&Trusted_Connection={Trusted_Connection}"
engine = create_engine(connection_string)
print("Connection successful!")


# Initialize SparkSession
spark = SparkSession.builder.appName("PySpark Practice").getOrCreate()

# Define the schema correctly
Schema = StructType([
    StructField("Id", IntegerType(), True),
    StructField("Name", StringType(), True),
    StructField("DeptId", StringType(), True)
])

# Create a DataFrame with sample data
df = spark.createDataFrame([
    (1, "a", "aa"),
    (1, "s", "ss"),
    (2, "d", "dd"),
    (2, "d", "dd"),
    (3, "h", "gg"),
    (4, "j", "h"),
    (5, "k", "jj"),
    (5, "k", "jj"),
    (7, "o", "ww"),
    (8, "u", "qq"),
    (9, "t", "aa")
], schema=Schema)
#remove duplicates
df = df.dropDuplicates()
# Show the DataFrame
df.show()
spark.stop()