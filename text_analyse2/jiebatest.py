#-*- coding:utf-8 -*-


#jieba 分词
import jieba
import jieba.analyse

seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
print "Full Mode:", "/ ".join(seg_list) #全模式

seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
print "Default Mode:", "/ ".join(seg_list) #精确模式

seg_list = jieba.cut("他来到了网易杭研大厦") #默认是精确模式
print ", ".join(seg_list)

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #搜索引擎模式
print ", ".join(seg_list)


w= open('result.txt','w')

s= '圣诞消费旺季即将到来，不得不推迟出货'
content=open('extract.txt').read()

seglist = list(jieba.cut(s,cut_all=False))
print ",".join(seglist)
for i in seglist:
    w.write(i.encode('utf-8'))#或者 w.write(i.encode('gbk'))
    w.write(',')
w.close()

#jieba增加自己的用户词典
#jieba.load_userdict(file_name) # file_name为自定义词典的路径

import sys
sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg

test_sent = "李小福是创新办主任也是云计算方面的专家;"
test_sent += "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类型"
words = jieba.cut(test_sent)
print type(words)

for w in words:
    print w


result = pseg.cut(test_sent)

for w in result:
    print w.word, "/", w.flag, ", ",


print "\n========"

terms = jieba.cut('easy_install is great')
for t in terms:
    print t
print '-------------------------'
terms = jieba.cut('python 的正则表达式是好用的')
for t in terms:
    print t

import jieba.analyse
strx = '网络让我们之间的距离变的如此之近，也同时让我们变的如此遥远。世界上最远的距离不是南极到北极，也不是喜马拉雅之巅到马里亚纳之渊；而是相对而坐，却各自忙着刷手机。暂别网络世界，去和爱人道一句早安，去和朋友聊一夜往事，去和家人吃一顿饭，其实也是挺好的'
s= '结巴分词是一个Python下的中文分词组件'
rt = jieba.analyse.extract_tags(strx,5)
print jieba.analyse.extract_tags(s,2)  #这个样是按照列表的形式进行的输出，就和之前遇到的一样，不是编码的问题，而是关键词在列表中，才导致的这种问题。
for r in rt:
   print r