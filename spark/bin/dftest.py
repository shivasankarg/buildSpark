from pyspark.sql import SparkSession
import pyspark.sql
from pyspark.sql import functions

sqlContext = SparkSession.builder.appName("PythonSQL").config("spark.some.config.option", "some-value").getOrCreate()

df = sqlContext.read.json("/home/seamus4318/qw/spark/examples/src/main/resources/people.json")
# string_length_udf = pyspark.sql.functions.udf(lambda line: len(line), pyspark.sql.types.LongType())
# df.filter(string_length_udf(df["name"])>3).show()
df.filter(df['age'] > 21).show()