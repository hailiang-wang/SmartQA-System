#-- coding:utf-8 --#
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkContext
spark=SparkSession \
    .builder \
    .appName("sparkSession") \
    .getOrCreate()
#.config("spark.some.config.option", "some-value") 可有可无，不设置的情况下就是默认情况。
df=spark.read.json('../data/people.json')

df.show()
print '-------'
df.take(1) #这是什么意思？
print '--------'
df.printSchema()
df.select(df['name'],df['age']).show()
#df.select(df['name'], df['age'] ).show()

df.filter(df['age']>20).show()
df.groupby(df['age']).count().show()

#执行sql必须是要产生视图执行如下函数
df.createOrReplaceTempView('people')
sqldf=spark.sql('select * from people')
sqldf.show()
#产生全局临时视图

# df.createGlobalTempView('people')
# spark.sql("select * from global_tem.people").show()
# 为什么出错没搞清

#datafram 与RDD的交互
#RDD仍然要作为一种必须要学的数据结构
#sc=SparkContext(appName="rddtest")这种数据结构就不可取了
sc=spark.sparkContext
lines=sc.textFile('../data/people.txt')
parts=lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))#冒号前是参数，冒号后表达式就是返回值
#RDD是对象的集合，而DataFrame是

# Infer the schema, and register the DataFrame as a table.
#schemaPeople = spark.createDataFrame(people) #两种产生datafram结构的方式
schemaPeople=people.toDF()
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# The results of SQL queries are Dataframe objects.
# rdd returns the content as an :class:`pyspark.RDD` of :class:`Row`.
teenNames = teenagers.rdd.map(lambda p: "Name: " + p.name).collect()
for name in teenNames:
    print(name)


#是否可以从ndarray中产生datafram,从dataframe，series中转为DataFrame
#必须要解决spark算法数据输入的问题。

df = spark.read.load("../data/users.parquet")
#df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")
df.show()

peopleDF = spark.read.json("../data/people.json")

# DataFrames can be saved as Parquet files, maintaining the schema information.
peopleDF.write.parquet("../data/people.parquet")

# Read in the Parquet file created above.
# Parquet files are self-describing so the schema is preserved.
# The result of loading a parquet file is also a DataFrame.
parquetFile = spark.read.parquet("../data/people.parquet")

# Parquet files can also be used to create a temporary view and then used in SQL statements.
parquetFile.createOrReplaceTempView("parquetFile")
teenagers = spark.sql("SELECT name FROM parquetFile WHERE age >= 13 AND age <= 19")
