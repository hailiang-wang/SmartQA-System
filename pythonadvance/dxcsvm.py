import  pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np



datas=pd.read_excel('../data/sampling.xlsx')
X=datas.iloc[:,1].as_matrix()
y=datas.iloc[:,0].as_matrix()
# print X
# print y
print X.shape
# import  xlrd
# datas=xlrd.open_workbook('sampling.xlsx')
# table = datas.sheet_by_name(u'Sheet1')
# X= np.matrix(table.col_values(4))
# y=np.matrix(table.col_values(0))
# print X
# print y
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
svr_rbf.fit(X, y)
y_rbf = svr_rbf.predict(X)
svr_lin.fit(X, y)
y_lin = svr_lin.predict(X)
svr_poly.fit(X, y)
y_poly = svr_poly.predict(X)
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.hold('on')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
