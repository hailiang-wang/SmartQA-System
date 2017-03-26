
# -*- coding: UTF-8 -*-

import re
print re.match('www', 'www.runoob.com').span()  # 在起始位置匹配
print re.match('www','www.runoob.com')
#print re.match('com', 'www.runoob.com').span()        # 不在起始位置匹配,re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。


import re

test = "我是123周小旭,来自1bd江西ab九江"

result = re.findall(ur'[\u4e00-\u9fa5]', test.decode('utf-8'))

print result


print ''.join(result)

result=re.findall(r'[0-9]',test)
print result

result=re.findall(r'[a-z]',test)
print result

text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.search(r'\shan(ds)ome\s', text)
if m:
    print m.group(0), m.group(1)
else:
    print 'not search'


text = "JGood is a handsome boy, he is cool, clever, and so on..."
print re.sub(r'\s+', '-', text)
#re.split(r'\s+', text)；将字符串按空格分割成一个单词列表

#re.findall可以获取字符串中所有匹配的字符串。如：re.findall(r'\w*oo\w*', text)；获取字符串中，包含'oo'的所有单词。

text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print regex.findall(text)   #查找所有包含'oo'的单词
print regex.sub(lambda m: '[' + m.group(0) + ']', text) #将字符串中含有'oo'的单词用[]括起来。
inputStr = "hello 123 world 456"
replacedStr = re.sub("\d+", "222", inputStr)
print replacedStr