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
print 'matrix'
d= np.array([[1,2,3],[4,5,6]])
print d.cumsum(0)  #0是指一列，1是指一行
print d.cumsum(1)
print d.cumprod(1)
print d.cumprod(0)

e=np.random.randn(3,4)
print type(e) #np产生的都是一维或者高维数组

t1=np.linspace(0,2,10)
print t1
t2=np.linspace(-1,1,20)
print t1,t2
#t=np.concatenate(t1,t2)
#print t



a = np.matrix([ [1, 2, 3, 4],
                       [5, 5, 6, 8],
                       [7, 9, 9, 1],
                       [4, 6, 7, 1]
                     ])

#矩阵加减法：
e = a + a
#or
e = a - a

#矩阵乘法:
b = a * a            #not matrix multiplication!
print type(b)
#or
c = np.dot(a, a)          #matrix multiplication
#or
d = a
np.dot(a, a, d)          #matrix multiplication

#转置矩阵(transpose)
g = a.transpose()
#or
h = a.T               #not matrix transpose!

#逆矩阵(inverse)
#The inverse of a matrix A is the matrix B such that AB=I where I is the identity matrix consisting of ones down the main diagonal. Usually B is denoted B=A-1 .
#In SciPy, the matrix inverse of the Numpy array, A, is obtained using linalg.inv (A) , or using A.I
f = np.linalg.inv(a)
#or
f = a ** (-1)
#or
f = a.I

#行列式(determinant)
j = np.linalg.det(a)

#伴随矩阵(adjoint)
#(need more test)
m = np.dot(np.linalg.det(a), np.linalg.inv(a))	# A-1 = A'' / |A|  ==>   A''= A-1|A|

#矩阵范数(matrix norms)
k = np.linalg.norm(a)

l1=[1,2,3]
l2=[1,2,3]
l3=[1,2,3]
l1=np.array(l1)
l2=np.array(l2)
l3=np.array(l3)
l=list((l1+l2+l3)/3)
print l








