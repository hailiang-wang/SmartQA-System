#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datas=pd.read_excel('../data/sampling.xlsx')
# print datas
data=datas.iloc[:,1:].as_matrix()
target=datas.iloc[:,0].as_matrix()
print data.shape

print type(target)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(data,target)
# print model.predict(data[0])
#
print np.matrix(model.coef_)
from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(model, data, target, cv=10)

fig, ax = plt.subplots()
ax.scatter(target, predicted)
ax.plot([target.min(), target.max()], [target.min(), target.max()], 'g', lw=1)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
print model.score(data,target)