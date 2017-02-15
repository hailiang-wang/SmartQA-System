import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)
for i in range(1,6):
    for j in range(1,6):
        ax.scatter(i,j)

ax.plot([0,5],[0,5],'k',lw=4)
plt.show()