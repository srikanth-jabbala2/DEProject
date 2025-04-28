from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, concat

spark = SparkSession.builder.appName("FixNativeIO").getOrCreate()

#sample data

data = [(1, 'pullajjjjjjjjjjjjjjjjjjjjjhnnnnnnnnnnnnyya', '1/323', 'Churchst', 9988202202),
        (2, 'kanth', '1/324', 'Templstt', 9988202202),
        (3, 'Sri', '1/325', 'masquestt', 9988202202),
        (4, 'Yellamma', '1/326', 'gurustt', 9988202202),
        (5, 'ooooooooooooooooooooooo', '1/327', 'jainstt', 9988202202),
        (6, 'Kolli', '1/328', 'Churchst', 9988202202)]

#structFiled and structType
schema = StructType([
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('address', StringType(), True),
    StructField('street', StringType(), True),
    StructField('phone', LongType(), True)
])

df = spark.createDataFrame(data=data, schema=schema)
#show
df.show(truncate=True)
df.printSchema()

#withcolumn

df = df.withColumn('phone', col('phone').cast(StringType()))
df1 = df.withColumn('phone', concat(lit('+091 '), col('phone'))) #concat is used to concatenate two columns using withcolumn
df2 = df1.withColumn('Country', lit('India')) #lit is used to add a constant value to the column
df3 = df2.withColumnRenamed('phone', 'PhoneNumber') #withCOlumnRenamed is used to rename the column
df3.show(truncate=True)
df3.printSchema()