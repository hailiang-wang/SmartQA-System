from keras.models import Sequential
from keras.layers.core import Dense ,Dropout,Activation
from keras.optimizers import SGD
import pandas as pd
import  matplotlib.pyplot as plt

print 'qx'
datas=pd.read_excel('../data/sampling.xlsx')
X=datas.iloc[:,1:].as_matrix()
y=datas.iloc[:,0].as_matrix()
print y
model= Sequential()
model.add(Dense(26,input_dim=26))
model.add(Activation('linear'))

model.add(Dense(26,input_dim=26))
model.add(Activation('linear'))
model.add(Dropout(0.5))
model.add(Dense(1,input_dim=26))
#model.add(Activation('linear'))
# sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='mean_squared_error',optimizer=sgd,metrics=["accuracy"])
model.compile(loss='mean_squared_error', optimizer='rmsprop')
model.fit(X, y, batch_size=5, nb_epoch=100, shuffle=True,verbose=0,validation_split=0.2)
score=model.evaluate(X,y,batch_size=16)
p=model.predict(X,batch_size=16,verbose=0)
print p

fig, ax = plt.subplots()
ax.scatter(y, p)

ax.plot([y.min(),y.max()],[y.min(),y.max()],'g',lw=4)
plt.show()


#from keras.models import Sequential
#
# from keras.layers import LSTM, Dense
#
# import numpy as np
#
# data_dim = 16
#
# timesteps = 8
#
# nb_classes = 10
#
# # expected input data shape: (batch_size, timesteps, data_dim)
#
# model = Sequential()
#
# model.add(LSTM(32, return_sequences=True,
#
# input_shape=(timesteps, data_dim)))
#
# model.add(LSTM(32, return_sequences=True))
#
# model.add(LSTM(32))
#
# model.add(Dense(10, activation='softmax'))
#
# model.compile(loss='categorical_crossentropy',
#
# optimizer='rmsprop',
#
# metrics=['accuracy'])
#
# # generate dummy training data
#
# x_train = np.random.random((1000, timesteps, data_dim))
#
# y_train = np.random.random((1000, nb_classes))
#
# # generate dummy validation data
#
# x_val = np.random.random((100, timesteps, data_dim))
#
# y_val = np.random.random((100, nb_classes))
#
# model.fit(x_train, y_train,
#
# batch_size=64, nb_epoch=5,
#
# validation_data=(x_val, y_val))
