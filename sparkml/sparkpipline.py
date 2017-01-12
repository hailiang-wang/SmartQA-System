#-- coding:utf-8 --#
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.sql import SparkSession

spark=SparkSession \
    .builder \
    .appName('pipline') \
    .getOrCreate()

# Prepare training documents from a list of (id, text, label) tuples.
#tuples的一个list表
#spark本身具备了sqlContext的功能
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])

# Configure an ML pipeline, which consists of three stages: tokenizer, hashingTF, and lr.
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

# Fit the pipeline to training documents.
model = pipeline.fit(training)
#算法部分也要依据固有的dataframe格式才可以。
# Prepare test documents, which are unlabeled (id, text) tuples.
test = spark.createDataFrame([
    (4, "spark i j k"),
    (5, "l m n"),
    (6, "spark hadoop spark"),
    (7, "apache hadoop")
], ["id", "text"])

# Make predictions on test documents and print columns of interest.
prediction = model.transform(test)
print prediction
selected = prediction.select("id", "text", "probability", "prediction")
selected.show()
print selected.collect() #将DataFrame按照row的格式输出

for row in selected.collect():
    print row
    rid, text, prob, prediction = row
    print("(%d, %s) --> prob=%s, prediction=%f" % (rid, text, str(prob), prediction))


#需重点看一下spark.read DataFrame东西。
#疑问一、写入的时候为什么报错
#疑问二、如何将dataframe结构转化为算法需要的结构。label，features,可以设定。
#是否可以使用RDD改变map映射，再用raw的方式赋予label与raw的方式