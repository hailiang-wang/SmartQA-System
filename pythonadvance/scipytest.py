from scipy import stats
X=stats.norm.rvs(0,size=500,scale=0.1)
#X =stats.norm(loc=1.0,scale=2.0,size = 100)


print stats.norm.fit(X)
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
fs_meetsig = np.random.random(30)
fs_xk = np.sort(fs_meetsig)
fs_pk = np.ones_like(fs_xk) / len(fs_xk)
fs_rv_dist = stats.rv_discrete(name='fs_rv_dist', values=(fs_xk, fs_pk))

plt.plot(fs_xk, fs_rv_dist.cdf(fs_xk), 'b-', ms=12, mec='r', label='friend')
plt.show()

age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat_percent = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
age = np.array(age)
fat_percent = np.array(fat_percent)
data = np.vstack([age, fat_percent]).reshape([-1, 2])

print(stats.describe(data))

for key, value in stats.describe(data)._asdict().items():
    print(key, ':', value)

# shannon_entropy = stats.entropy(ij/sum(ij), base=None)
# print(shannon_entropy)