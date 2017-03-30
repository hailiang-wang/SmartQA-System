# -*- coding: utf-8 -*-
import jieba, os
import codecs
from gensim import corpora, models, similarities
from pprint import pprint
from collections import defaultdict
import sys
import pickle

reload(sys)
sys.setdefaultencoding('utf-8')


def print_dict(dict):
    for key in dict:
        print type(key), key, str(dict[key]),
    print


def test3():
    ''''
    gensim学习之Dictionary
    '''
    a = [['一','一','二'],['一','二','三']]
    b = ['一','一','三','四','四']
    dictionary = corpora.Dictionary(a)
    print "########dictionary信息##########"
    print str(dictionary) #
    print "字典，{单词id，在多少文档中出现}"
    print dictionary.dfs #字典，{单词id，在多少文档中出现}
    print "文档数目"
    print dictionary.num_docs #文档数目
    print "dictionary.items()"
    print_dict(dict(dictionary.items())) #
    print "字典，{单词id，对应的词}"
    print_dict(dictionary.id2token) #字典，{单词id，对应的词}
    print "字典，{词，对应的单词id}"
    print_dict(dictionary.token2id) #字典，{词，对应的单词id}
    print "所有词的个数"
    print dictionary.num_pos #所有词的个数
    print "每个文件中不重复词个数的和"
    print dictionary.num_nnz #每个文件中不重复词个数的和
    print "########doc2bow##########"
    #dictionary.add_documents([b])
    #allow_update->更新当前字典；return_missing->返回字典中不存在的词
    #result为b文章转换得到的词袋，列表[(单词id，词频)]
    result, missing = dictionary.doc2bow(b, allow_update=False, return_missing=True)
    print "词袋b，列表[(单词id，词频)]"
    print result
    print "不在字典中的词及其词频，字典[(单词，词频)]"
    print_dict(missing)
    print "########bow信息##########"
    for id, freq in result:
        print id, dictionary.id2token[id], freq
    print "########dictionary信息##########"
    #过滤文档频率大于no_below，小于no_above*num_docs的词
    dictionary.filter_extremes(no_below=1, no_above=0.5, keep_n=10)

    return

test3()


