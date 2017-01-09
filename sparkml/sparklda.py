#--coding:utf-8 --#
from pyspark.ml.clustering import LDA
from pyspark.sql import SparkSession
spark=SparkSession \
    .builder \
    .appName('sparklda') \
    .getOrCreate()

#libsvm是一种什么样的数据结构为什么要采用这样的方式
#为什么一般的txt文件不可以呢？？？？？
# Loads data.
dataset = spark.read.format("libsvm").load("../data/sample_lda_libsvm_data.txt")

# Trains a LDA model.
lda = LDA(k=10, maxIter=10)
model = lda.fit(dataset)

ll = model.logLikelihood(dataset)
lp = model.logPerplexity(dataset)
print("The lower bound on the log likelihood of the entire corpus: " + str(ll))
print("The upper bound bound on perplexity: " + str(lp))

# Describe topics.
topics = model.describeTopics(3)
print("The topics described by their top-weighted terms:")
topics.show(truncate=False)

# Shows the result
transformed = model.transform(dataset)
transformed.show(truncate=False)