#-- coding:utf-8 --#
from pyspark.sql import SparkSession
spark=SparkSession \
    .builder \
    .appName("sparkSession") \
    .getOrCreate()
#.config("spark.some.config.option", "some-value") 可有可无，不设置的情况下就是默认情况。
df=spark.read.json('../data/people.json')

df.show()

#df.take(1) 这是什么意思？

df.printSchema()
df.select(df['name'],df['age']).show()
#df.select(df['name'], df['age'] ).show()

df.filter(df['age']>20).show()
df.groupby(df['age']).count().show()
df.createOrReplaceTempView('people')
sqldf=spark.sql('select * from people')
sqldf.show()


sc=spark.sparkContext
