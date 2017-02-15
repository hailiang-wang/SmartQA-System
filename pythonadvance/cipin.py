# from numpy import array
# from math import sqrt
#
# from pyspark.mllib.clustering import KMeans, KMeansModel
# from pyspark import  SparkContext
# sc = SparkContext("local",appName="KMeans")
#
# data = sc.textFile("D:\\PycharmProjects\\data\\mllib\\kmeans_data.txt")
# parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))
#
# # Build the model (cluster the data)
# clusters = KMeans.train(parsedData, 2, maxIterations=10,
#                         runs=10, initializationMode="random")
#
# # Evaluate clustering by computing Within Set Sum of Squared Errors
# def error(point):
#     center = clusters.centers[clusters.predict(point)]
#     return sqrt(sum([x**2 for x in (point - center)]))
#
# WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
# print("Within Set Sum of Squared Error = " + str(WSSSE))
#
# # Save and load model
# clusters.save(sc, "D:\\PycharmProjects\\KmeansModel")
# sameModel = KMeansModel.load(sc, "D:\\PycharmProjects\\KmeansModel")


from pyspark import SparkContext

logFile = "D:\spark-1.6.2-bin-hadoop2.6\README.md"
sc = SparkContext("local","Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i"%(numAs, numBs))



# from pyspark.ml.clustering import KMeans
#
# from pyspark.sql import SparkSession
#
# # Loads data.
#
# spark = SparkSession \
#     .builder \
#     .appName("mlkmeans") \
#     .getOrCreate()
# dataset = spark.read.format("libsvm").load("D:\\PycharmProjects\\data\\mllib\\sample_kmeans_data.txt")
#
# # Trains a k-means model.
# kmeans = KMeans().setK(2).setSeed(1)
# model = kmeans.fit(dataset)
#
# # Evaluate clustering by computing Within Set Sum of Squared Errors.
# wssse = model.computeCost(dataset)
# print("Within Set Sum of Squared Errors = " + str(wssse))
#
# # Shows the result.
# centers = model.clusterCenters()
# print("Cluster Centers: ")
# for center in centers:
#     print(center)


# from pyspark import SparkContext
#
# sc = SparkContext('local')
# doc = sc.parallelize([['a','b','c'],['b','d','d']])
# words = doc.flatMap(lambda d:d).distinct().collect()
# word_dict = {w:i for w,i in zip(words,range(len(words)))}
# word_dict_b = sc.broadcast(word_dict)
#
# def wordCountPerDoc(d):
#     dict={}
#     wd = word_dict_b.value
#     for w in d:
#         if dict.has_key(wd[w]):
#             dict[wd[w]] +=1
#         else:
#             dict[wd[w]] = 1
#     return dict
# print doc.map(wordCountPerDoc).collect()
# print "successful!"
