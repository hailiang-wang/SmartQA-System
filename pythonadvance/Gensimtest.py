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

for i in fab(5):
    print i