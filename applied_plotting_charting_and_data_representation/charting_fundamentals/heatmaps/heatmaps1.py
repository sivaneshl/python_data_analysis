import matplotlib.pyplot as plt
import numpy as np

Y = np.random.normal(loc=0, scale=1, size=10000)
X = np.random.random(size=10000)

plt.hist2d(X, Y,  bins=100)
plt.colorbar()

plt.show()