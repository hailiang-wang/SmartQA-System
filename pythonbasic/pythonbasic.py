#-- coding:utf-8 --#

#列表自动生成

l=range(10)
print l
l2=l[:-9-1:-1]
print l2
l1=l[9:2:-2]#第三个参数是间隔
print l1

print '\\' #""是一样的不需要变
print r'\\' #r中没有转义字符
print u'\\' #u是unicode编码普通的是ascii编码
print '\n'
print '\t'

a = 'python'
print 'hello,', a and 'world' #在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b
b = ''
print 'hello,', b or 'world' #在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。

c=['a','b','c']
for i,j in enumerate(c):
    print i,'-',j
for i ,j in zip(range(1,len(c)+1),c):
    print i ,'-',j

print filter(lambda s:s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END']) #冒号前面是函数参数，冒号后边是表达式也是return值。
#print type(None)
#python中的map函数
def format_name(s):
    return s[0].upper()+s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])#函数返回新的元素
#python中的filter函数
import math
def is_sqr(x):
    return x and math.sqrt(x)%1==0
print is_sqr(100)
print filter(is_sqr, range(1, 101)) #函数返回布尔类型的值
#python中的reduce函数
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])


str="abcd"
l=list(str)
print l

a="a"
b="b"
#print str(a) 报错
c=100
a=12
print chr(a)
a='10'
print int(a)
#print a+b+chr(c)

#print int(a)+int(b)+c 报错
i=int(raw_input('请输入i：'))
l=range(i)
for i in range(i):
    l[i]=i+2

print l
fo=open('../data/people.txt')
print type(fo)
for i in fo:
    i.strip(',') #是删除''引号中的字符串
    i=i.split(',')
    print type(i)
    for i in i:
        print i



def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument

# 调用函数
temp_convert("xyz")

a=[[1,2,3],[4,5,6]]
print type(a)

dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
print type(dataSet)

print range(1,5)
print range(6,10)
print range(1,5)+range(6,10) #列表相加不是俩俩相加，而是合成一个更长的list

i='####口疮####飞滋####口炎疮####复发性口疮####复发性'
i=i.strip('####')
print i
j='###我们###你们'
j=j.strip('####')
print j