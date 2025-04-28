import os
from pyspark.sql import SparkSession

# Set up environment for Windows
os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['PATH'] += os.pathsep + "C:\\hadoop\\bin"

spark = SparkSession.builder \
    .appName("FixNativeIO") \
    .config("spark.hadoop.io.nativeio.enabled", "false") \
    .getOrCreate()

# Create dummy DataFrame
data = [(1, 'Sri', 'Out'), (2, 'Kanth', 'Put')]
schema = ['id', 'name', 'status']
df = spark.createDataFrame(data=data, schema=schema)
df.show()

# Save to CSV
df.write.csv(path="C:/tmp/output", header=True, mode='append')
print('Data written as csv file successfully')

# Read it back
df2 = spark.read.csv(path="C:/tmp/output", header=True, inferSchema=True)
df2.show()