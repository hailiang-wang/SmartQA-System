import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


fig=plt.figure()
ax=fig.add_subplot(111)
for i in range(1,6):
    for j in range(1,6):
        ax.scatter(i,j)

ax.plot([0,5],[0,5],'k',lw=4)
plt.show()

dates=pd.date_range('2/17/2017',periods=1000)
nd=pd.DataFrame(np.random.randn(1000,4),index=dates,columns=['a','b','c','d'])
print nd
nd=nd.cumsum()
plt.figure()
nd.plot()
plt.show()
