# # import os

# # # Make sure Spark uses your correct Python
# # os.environ["PYSPARK_PYTHON"] = r"C:\Users\jabbala\AppData\Local\Programs\Python\Python312\python.exe"
# # os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\jabbala\AppData\Local\Programs\Python\Python312\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
df.show()


# import sys
# print(f"Running with Python: {sys.executable}")
