#-*- coding: utf-8 -*-
import numpy as np

a=np.array([2,0,1,5])
print a
print a[:3]
print a.min()
a.sort()
b=np.array([[1,2,3],[4,5,6]])
print (b*b) #是点乘不是传统意义上的矩阵相乘

print type(b) #numpy 仍然是传统意义上的数组