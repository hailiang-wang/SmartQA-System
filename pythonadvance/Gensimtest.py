#-*- coding:utf-8 -*-

import gensim,logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)

sentences=[['first','sentence'],['second','sentence']]

model=gensim.models.Word2Vec(sentences,min_count=1)

print(model['first'])
