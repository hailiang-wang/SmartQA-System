#encoding=utf-8
#from __future__ import unicode_literals
#import sys
#sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

print('关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

f = open("../data/ndy.txt","r")
s = f.read()
print type(s)

for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print "Full Mode:", "/ ".join(seg_list) #全模式