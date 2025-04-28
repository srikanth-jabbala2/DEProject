from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType, ArrayType, IntegerType
from pyspark.sql.functions import col, explode, lit, concat, when, round, count, sum as _sum, date_sub, split

spark = SparkSession.builder.getOrCreate()

#arrayType
data = [('abc', [1,23]), 
        ('def', [2,24]),
        ('ghi', [3,25]),
        ('jkl', [4,26]),
        ('mno', [5,27]),
        ('pqr', [6,28])]

data1 = [('sr')]

schema = StructType([
    StructField('id', StringType(), True),
    StructField('numbers', ArrayType(IntegerType()), True)
])

data1 = [(1, 'Yerranna', ('doctor,actor')), (2, 'veerabadra', ('scientist,engineer')), (3, 'Sri', ('teacher,doctor'))]
schema1 = StructType([
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('professions', ArrayType(StringType()), True)
])

#explode
df = spark.createDataFrame(data=data1, schema=schema1)
df1 = df.withColumn('professions', explode(col('professions')))
#split and array
df2 = df.withColumn('professions', split(col('professions'), ','))
df2.show(truncate=True)

df2.printSchema()