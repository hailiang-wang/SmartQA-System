#-*- coding:utf-8 -*-
import  matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data=pd.read_excel('../data/Folds5x2_pp.xlsx')
print data.shape
X=data.iloc[:,0:4]
y=data.iloc[:,4]


from sklearn.cross_validation import  train_test_split

X_train,x_test,y_train,y_test=train_test_split(X,y)
#print X_train
#print y_train
#print x_test
#print y_test


model=LinearRegression()
model.fit(X_train,y_train)
print 'sucess'
y_pred=model.predict(x_test)

from sklearn import metrics
#print model.score(X,y)

# 用scikit-learn计算MSE
print "MSE:",metrics.mean_squared_error(y_test, y_pred)
# 用scikit-learn计算RMSE
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred))

from sklearn.model_selection import cross_val_predict
print 'sucess'
y_pred=cross_val_predict(model,X,y,cv=10)

print "MSE",metrics.mean_squared_error(y,y_pred)
print "RMSE:",np.sqrt(metrics.mean_squared_error(y,y_pred))

ax=plt.subplot()
ax.scatter(y,y_pred)
ax.plot([y.min(),y.max()],[y.min(),y.max()])
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()