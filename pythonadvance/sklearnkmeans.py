#-*- coding:utf-8 -*-
import pandas
import matplotlib.pyplot as plt

inputfile='../data/sampling.xlsx'
outputfile='../data/outputfile.xlsx'
data=pandas.read_excel(inputfile)
print data.index #可以同过index_col设置index的。
#print data.values
#data=data[2:]
data_zs=1.0*(data-data.mean())/data.std()


from sklearn.cluster import KMeans
model=KMeans(n_clusters=100,n_jobs=1,max_iter=500)
model.fit(data_zs)
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter()

t=pandas.concat([data,pandas.Series(model.labels_,index=data.index)],axis=1)
t.columns=list(data.columns)+[u'聚类类别']

#print type(t)
#print t

#print len( model.labels_)
r1=pandas.Series(model.labels_).value_counts()
#r1.index=range(100)
#print len(model.labels_)
#print model.cluster_centers_
r2=pandas.DataFrame(model.cluster_centers_)
r=pandas.concat([r2,r1],axis=1)
r.columns=list(data.columns) + [u'聚类类别']
#print r


l= r[r[u'聚类类别']<2].index
#print l
#print r
l=l.tolist()
# print type(l)
# print l
# t=t.iloc[l,:]
# print t
#t=t[t[u'聚类类别'] in l]
# print set(l)
# print type(t[u'聚类类别'])
t=t[ t[u'聚类类别'].isin(l)]


# for i in l:
#     (t[t[u'聚类类别']==i].index)
#     t[t[u'聚类类别']==i]
#     r=r.append(t[t[u'聚类类别']==i])

#r=r[99:]

#print r
#print data(x)
# for i in x:
#     print data(index=i)
t.to_excel(outputfile)
