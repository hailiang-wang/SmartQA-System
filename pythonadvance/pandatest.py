#-- coding:utf-8 --#
import pandas as pd
from pandas import Series,DataFrame

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
print s
print d
sd=pd.concat((s,d),axis=1)
print sd

d.head(1)
d.tail(1)
#d.to_excel('../data/test.xlsx')
r=pd.read_excel('../data/test.xlsx')
print r