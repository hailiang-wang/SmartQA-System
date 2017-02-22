#-*- coding:utf-8 -*-

import gensim,logging
import numpy as np
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)

sentences=[['first','sentence'],['second','sentence']] #说明了模型的输入是什么形式的,必须是这种列表性质的

model=gensim.models.Word2Vec(sentences,min_count=1,size=100) #min_count是可以忽略的出现次数少的词，因此当min_count设置为2时，报错，因为first被忽略了。size代表向量的维度。




print(model['first'])
print model.similarity('first','second')
print model.most_similar(positive=['first'], negative=['sentence'])
print ("first sentence second sentence , 有哪个是不匹配的? word2vec结果说是:"+model.doesnt_match("first sentence second sentence".split()))

print model['first'].shape

#没有理解
class TextLoader(object):
    def __init__(self):
        pass

    def __iter__(self):
        input = open('corpus-seg.txt', 'r')
        line = str(input.readline())
        counter = 0
        while line != None and len(line) > 4:
            # print line
            segments = line.split(' ')
            yield segments
            line = str(input.readline())

#没有理解
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

#sentences = MySentences('/some/directory') # a memory-friendly iterator
#model = gensim.models.Word2Vec(sentences)

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
print type(fab(5))
next(fab(5))
for i in fab(5):
    print i
from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
             "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]

 # remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
         frequency[token] += 1
print 'sucess'
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
from pprint import pprint  # pretty-printer
pprint(texts)
print type(texts)

dictionary = corpora.Dictionary(texts)
#dictionary.save('../tmp/deerwester.dict')  # store the dictionary, for future reference
print(dictionary)
print(dictionary.token2id)
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)

corpus = [dictionary.doc2bow(text) for text in texts]
#corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)  # store to disk, for later use
print(corpus)
