#-*- coding:utf-8 -*-
import numpy
import random
import pandas as pd

print numpy.random.randn(6,5) #服从正太分布的，均值为0的矩阵
print numpy.random.rand(3,4) #服从正态分布的，0,1之间的矩阵

print random.random()

print random.uniform(10, 20)

print random.randint(12, 20)

print random.choice('abcdefg&#%^*f')

print random.sample('abcdefghij',3) #选取特定数量的字符

import string

print string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).replace(" ","")

print random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )

items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
print items
