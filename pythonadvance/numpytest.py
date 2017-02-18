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


a=np.arange(1,4).cumprod() #每个数取得是连乘就是阶乘了
print a
b=np.array([2]*3).cumprod() #2的一次方到2的三次方，里边是产生了3个2
print b

#np后边产生的都是数组
print np.linspace(1,2,10) #数组与列表的区别就在于没有逗号

print np.array([2]*3)
d= np.array([[1,2,3],[4,5,6]])
print d.cumsum(0)  #0是指一列，1是指一行
print d.cumsum(1)
print d.cumprod(1)
print d.cumprod(0)

e=np.random.randn(3,4)
print type(e) #np产生的都是一维或者高维数组

t1=np.linspace(0,2,10)
t2=np.linspace(-1,1,20)
#print t1,t2
t=np.concatenate(t1,t2)
print t