from pyspark.sql import *
from pyspark.sql.types import *
import os

# Set up environment for Windows
os.environ['HADOOP_HOME'] = "C:\\hadoop"
os.environ['PATH'] += os.pathsep + "C:\\hadoop\\bin"


spark = SparkSession.builder.\
        appName("FixNativeIO").\
        config("spark.hadoop.io.nativeio.enabled", "false").getOrCreate()
# help(spark.read.json)

data = [
    (1, 'Sri', 23, 'India'),
    (2, 'Kanth', 24, 'India'),
    (3, 'Yellamma', 25, 'africa'),
    (4, 'Pullamma', 26, 'India'),
    (5, 'Chinna', 27, 'India'),
    (6, 'Kolli', 28, 'India')
]
schema = StructType([
					StructField('id', IntegerType(), True),
					StructField('Name', StringType(), True),
					StructField('age', IntegerType(), True),
					StructField('country', StringType(), True)
                ])
df = spark.createDataFrame(data=data, schema=schema)

# #read json
# df = spark.read.json('samplejson.json', multiLine = True,schema = schema)

# # df.show(truncate = False)
# # df.printSchema()

# #write json file
# df.write.json(path ="c:/tmp/outputjson", mode='overwrite')
# df2 = spark.read.json(path ="c:/tmp/outputjson")
# df2.show(truncate = False)

#read parquet file

# df=spark.read.parquet(r'C:\Users\jabbala\OneDrive - DevOn India-NL BV\Documents\Big Data - Srikanth\DEproject\DEProject\parquerprac\*.parquet',\
#                       inferSchema=True, header=True)
# # df = spark.read.parquet(path = r'C:\Users\jabbala\OneDrive - DevOn India-NL BV\Documents\Big Data - Srikanth\DEproject\DEProject\parquerprac.parquet')
# df.show(truncate = False)
# print(df.count())

# #write parquet file
df.write.parquet(path="c:/tmp/outputparquet", mode='overwrite')
df2 = spark.read.parquet(r'c:/tmp/outputparquet/*.parquet',inferSchema=True, header=True)
df2.show()