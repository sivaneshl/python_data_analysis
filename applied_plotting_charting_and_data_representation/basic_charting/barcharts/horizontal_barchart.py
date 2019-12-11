import numpy as np
import matplotlib.pyplot as plt

linear_data = np.array(range(1,9))
quadratic_data = linear_data**2

plt.figure()
xvals = range(len(linear_data))

plt.barh(xvals, linear_data, height=0.3, color='blue')
plt.barh(xvals, quadratic_data, height=0.3, left=linear_data, color='red')

plt.show()