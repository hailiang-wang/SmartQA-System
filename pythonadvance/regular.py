
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

str='''江苏省人民医院心血管内科 感谢信56封礼物40个[图片]职　　称：副主任医师 副教授[图片]擅　　长：
心房颤动、室性心动过速与各种室上性心动过速的导管消融与缓慢性心律失常的起搏治疗
心房颤动、室性心动过速与各种室上性心动过速的导管消融与缓慢性心律失常的起搏治疗[图片]执业经历：
张凤祥，男，医学博士，副主任医师、副教授，硕士生导师；中国医师协会心律失常分会青委会副主任委员，中华医学会心电生理和起搏分会青年委员，中国医师协会心血管内科医师分会青年委员，中华医学会江苏省心血管病分会青年委员会副主委，中华全科医学杂志编委；2007年毕业于南京医科大学并任职于南京医科大学第一附属医院（江苏省人民医院）。熟练掌握各种心律失常的诊断与治疗。主要研究方向：心律失常的临床治疗与基础研究。擅长1）心房颤动、室性早搏、室性心动过速、房性心动过速、阵发性室上速、等心律失常的导管消融治疗；2) 房室传导阻滞、病态窦房结综合征等缓慢心律失常的起搏治疗；3）Brugada综合征、长QT综合征、短QT、儿茶酚胺敏感室速等心脏性猝死预防。发表学术论文50篇，其中SCI文章近20篇。主持国家自然科学基金3项，江苏省六大人才高峰课题1项，中国医师协会课题1项；参与973、十二五等重大科研课题；荣获江苏省卫生厅新技术引进二等奖2项。<< 收起'''
print str
str=str.replace('\n','')
print str
str1='''通过好大夫在线提前预约名大夫的办法

    准备去北京或者其他大城市看病或者做手术的人，可以提前通过好大夫在线联系好大夫，否则，直接去了这些名大夫的号很难挂。下边以去北京安贞找马长生治疗房颤为例说明办法：
，      
  第一，提前拍摄好自己的病历材料，（手头没有可以凭病号身份证去医院病案室复印）。要求最少提供：
             （1）发作时期的心电图或者记录有发作症状的24小时心电图报告页。
             （2）心脏彩超。必须带数据部分
             （3）血液生化全部项目报告单
             （4）你治疗期间做的其他价格高的检查，比如心脏CTA等等    
             （5）最近一次因为房颤住院的出院小结                                               
      图片要求拍摄清晰，可以适当掩盖住名字部分。
      写一份详细的生病状况和治疗情况说明，内容要有发病症状，所入医院名称和科室。大概治疗用药物，写上出院小结内大夫给的诊断结论还有出院大夫要求吃的药物。                                                   
  第二登陆马长生的好大夫在线的个人网站地址是    http://machangsheng.haodf.com/ （如果你找其他大夫看病就去其他大夫的网站）
  第三点击  网上咨询。一般都提示你注册，注册的时候所留手机号码必须真实有效。以后要用来接收大夫回复以后的短信通知。
  第四填写各种内容和上传图片
  第五，点击最下面的确定 等待大夫的回复
   大夫回复后，有时候他会提问你问题，也可能要求补充病历材料等，你可以根据情况继续上传和给出说明
 一般来说，一个注册号码一次可以得到3次提问机会，超过部分是要收费的。当然，到第三次的时候大夫如果认为有必要，一般会再给你三次机会。
 如果大夫认为你适合找他看病或者手术，一般他会给你一个住院管理大夫的电话，你电话过去说明是马长生叫你打的电话，要求给定病床。等他有病床了会提前通知你。这样你再去北京就不用等待了，免去了很多外地人到北京住院治疗的烦恼      

以下是心脏内科导管消融的好大夫

http://machangsheng.haodf.com/   马长生 北京安贞

http://dongjianzeng.haodf.com/   董建增 北京安贞

http://yaoyan.haodf.com/         姚焰   北京阜外

http://liuxu001.haodf.com/       刘旭 上海市胸科医院  心内科

http://wxqing1212.haodf.com/     王现青.河南省人民医院  心血管内科

http://huanghe1977.haodf.com/    黄鹤 武汉大学人民医院  心血管内科

http://xpliu71.haodf.com/        刘兴鹏 北京朝阳医院  心脏中心

http://jiangchenyang.haodf.com/  蒋晨阳 浙江大学医学院附属邵逸夫医院  心内科 

http://liushaowen.haodf.com/     刘少稳上海市第一人民医院  心内科
                         



以下是心脏外科用胸腔镜治疗房颤,的好大夫,                         
                                    
http://zhengzhe.haodf.com/       郑哲  北京阜外医院

http://mxu263.haodf.com/         孟旭  北京安贞医院   心脏外科中心

http://xuchunlei.haodf.com/      许春雷 北京安贞医院  心脏外科中心

http://meiju.haodf.com/          上海新华 梅举

http://chengyunge.haodf.com/     上海远大程云阁  国内唯一用胸腔镜做迷宫三手术的大夫，价格4.5万最便宜
        
                                        
                                          病友阵发房颤根据亲身经历整理
'''
print str1
str1=str1.replace('/r/n','')
print str1