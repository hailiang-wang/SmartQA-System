#-*- coding: utf-8 -*-
import pandas as pd
number = '../data/all_musicers.xlsx' #设定播放数据路径,该路径为代码所在路径的上一个目录data中.
data = pd.read_excel(number)

data1=data.iloc[:,0:10]#10位歌手的183天音乐播放量
#data2=data.iloc[:,10:20]
#data3=data.iloc[:,20:30]
#data4=data.iloc[:,30:40]
#data5=data.iloc[:,40:50]
import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.figure(1, figsize=(13, 26))#可设定图像大小
#plt.figure() #建立图像
p = data1.boxplot(return_type = 'dict') #画箱线图，直接使用DataFrame的方法.代码到这为止,就已经可以显示带有异常值的箱型图了,但为了标注出异常值的数值,还需要以下代码进行标注.
#for i in range(0,4):
x = p['fliers'][2].get_xdata() # 'flies'即为异常值的标签.[0]是用来标注第1位歌手的异常值数值,同理[i]标注第i+1位歌手的异常值.
y = p['fliers'][2].get_ydata()
y.sort() #从小到大排序
print x
print y
for i in range(len(x)):
  if i>0:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
  else:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))

plt.show() #展示箱线图
#输出结果如下:其中,+所表示的均是(统计学认为的)异常值.工作中,要结合数据应用背景, 距离箱型图上下界很近的可归为正常值.

for i in range(0,182):
    if data1.iloc[:,1][i]>125:
        data1.iloc[:,1][i]=(data1.iloc[:,1][i+1]+data1.iloc[:,1][i-1])/2
for i in range(0,182):
    if data1.iloc[:,2][i]>600:
        data1.iloc[:,2][i]=(data1.iloc[:,2][i+1]+data1.iloc[:,1][i-1])/2
for i in range(0,182):
    if data1.iloc[:,4][i]>225:
        data1.iloc[:,4][i]=(data1.iloc[:,4][i+1]+data1.iloc[:,4][i-1])/2
for i in range(0,182):
    if data1.iloc[:,7][i]>60:
        data1.iloc[:,7][i]=(data1.iloc[:,7][i+1]+data1.iloc[:,7][i-1])/2
for i in range(0,182):
    if data1.iloc[:,8][i]>2500:
        data1.iloc[:,8][i]=(data1.iloc[:,8][i+1]+data1.iloc[:,8][i-1])/2

data1.to_csv("train_innoraml.csv")