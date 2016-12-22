from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np

digits=load_digits()
print digits.data.shape
#print digits
#digits.reshape()
np.savetxt("filename.txt",digits)

plt.gray()
plt.matshow(digits.images[0])
plt.show()


