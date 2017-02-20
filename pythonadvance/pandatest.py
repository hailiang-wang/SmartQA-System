#-- coding:utf-8 --#
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

l=Series(data=[1,2,3])
print l
print l.data

for i in l.index:
    print  l[i] #只输出了data部分的数
print l[1:] #是对整个Series进行了切分。
#print l['a']
print l.index
m=[1,2,3,4]
print m    #列表与index不是同一种数据结构，index是一种对象类型，但是对index或者column赋值可以使用列表对其进行赋值。访问他们只能通过序号，可以是切片的形式。

s=Series([2,3,4],index=['b','a','c'])

d=DataFrame({'e':4,'d':5,'f':6},index=['a','b','c'])
print d.index
print d.columns
print d.values
print d.describe()
print s
print d
sd=pd.concat((s,d),axis=1)
print sd

d.head(1)
d.tail(1)
#d.to_excel('../data/test.xlsx')
r=pd.read_excel('../data/sampling.xlsx')
#print r

dates=pd.date_range('20170217',periods=2)
data=pd.DataFrame(np.random.randn(2,4),index=dates,columns=['a','b','c','d'])
print data
a=Series([1,2,3,4,None,5])
print a.isnull() #类型仍然是list
print type(a[a.isnull()]) #只出现结果是true的值，类型仍然是list ，pandas的任何一列都是Series

print a[range(1,3)] #Series的读取问题，可以根据列表序号进行读取。

