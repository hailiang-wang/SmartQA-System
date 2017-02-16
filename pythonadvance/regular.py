
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