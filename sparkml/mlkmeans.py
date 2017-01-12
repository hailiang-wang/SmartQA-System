#-- coding:utf-8 --#
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession
from pyspark.sql import Row
import pandas as pd
spark=SparkSession \
    .builder \
    .appName("kmeans") \
    .getOrCreate()

inputfile='../data/sampling.xlsx'
outputfile='../data/outputfile.xlsx'
data=pd.read_excel(inputfile)

print spark.createDataFrame(data).collect()  #spark通过pandas.DataFrame 转化为spark DataFrame ，df.toPandas()
#还可以通过tuple list与字典产生。

data=spark.read.format('csv').load('../data/sampling.csv') #直接读与createDataFrame方式进行。
data.show()
#dataset=spark.read.format('libsvm').load('../data/sample_kmeans_data.txt')
data=spark.sparkContext.textFile('../data/sampling.csv')
parts=data.map(lambda l: l.split(","))
dataset = parts.map(lambda p: Row(label=p[0], features=Vectors.dense([int(p[1]),int(p[2]),int(p[3]),int(p[4]),int(p[5]),int(p[6]),int(p[7]),int(p[8]),int(p[9]),int(p[10]),int(p[11]),int(p[12]),int(p[13]),int(p[14]),int(p[15]),int(p[16]),int(p[17]),int(p[18]),int(p[19]),int(p[20]),int(p[21]),int(p[22]),int(p[23]),int(p[24]),int(p[25])])))#冒号前是参数，冒号后表达式就是返回值
#RDD是对象的集合，而DataFrame是Vectors.dense(p[1:])

# Infer the schema, and register the DataFrame as a table.
#schemaPeople = spark.createDataFrame(people) #两种产生datafram结构的方式
datasets=spark.createDataFrame(dataset)

datasets.show()

# Trains a k-means model.
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(datasets)

# Evaluate clustering by computing Within Set Sum of Squared Errors.
wssse = model.computeCost(datasets)
print("Within Set Sum of Squared Errors = " + str(wssse))

# Shows the result.
centers = model.clusterCenters()

df=pd.DataFrame(centers)
print df.dtypes
df.to_excel(outputfile)

print("Cluster Centers: ")
for center in centers:
    print(center)

