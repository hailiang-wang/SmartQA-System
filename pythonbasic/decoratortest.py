#-*- coding:utf-8 -*-
from __future__ import division
def cmp_ignore_case(s1, s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1

#sorted函数是一个高阶函数，其包含的函数是一个比较函数，返回值是-1或者1
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case) #小的在前面是-1，是从小到大排列，反之从大到小；


def count():
    fs = []
    for i in range(1, 4):
        def f(j):  #本身已经是一个闭包，内部定义函数接受外部函数参数，并返回内部函数
            def g():
                return j*j
            return g
        r=f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3() #这里f1=f(1),f2=f(2),f3=f(3)

#装饰器的作用是写一个装饰器函数，能够一次满足所有有类似需求的函数。如：都有输出log的需求，那么写一个log装饰器即可

import time

def performance(f):
    def fn(*args,**kw):
        t1=time.time()
        r=f(*args,**kw)
        t2=time.time()
        print 'call %s()in %fs' % (f.__name__,(t2-t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()

import time

def performance(unit):
    def per_decorator(f):
        def fn(*args,**kw):
            t1=time.time()
            r=f(*args,**kw)
            t2=time.time()
            t=(t2-t1)*1000 if unit=='ms'else(t2-t1)    #这个地方有疑问
            print'call %s()in %f%s'%(f.__name__,t,unit)
            return r
        return fn
    return per_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

#偏函数的意义减少函数默认参数的设置 functools.partial是偏函数的基本格式
import functools

sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

#2.7使用3.几之后的功能使用 __future
print 10/3


print 10 / 3
print 10 // 3
#3.0之后unicode不需要加4

s = 'am I an unicode?'
print isinstance(s, unicode)