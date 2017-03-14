#-*- coding:utf-8 -*-
import nltk
# nltk.download()
sentence="I love python."
tokens=nltk.word_tokenize(sentence)


to=nltk.pos_tag(tokens)
for i in to:
    print i
h=nltk.pos_tag(['美'])

for i in h:
    print i[0]+'---'+i[1]
# from nltk.corpus import webtext
#
# webtext.fileids()      #得到语料中所有文件的id集合
#
# webtext.raw(fileid)  #给定文件的所有字符集合
#
# webtext.words(fileid) #所有单词集合
#
# webtext.sents(fileid)  #所有句子集合