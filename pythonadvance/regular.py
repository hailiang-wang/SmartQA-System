
# -*- coding: UTF-8 -*-

import re
print re.match('www', 'www.runoob.com').span()  # 在起始位置匹配
print re.match('www','www.runoob.com')
#print re.match('com', 'www.runoob.com').span()        # 不在起始位置匹配,re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。



