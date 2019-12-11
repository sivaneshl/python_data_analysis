import numpy as np
import matplotlib.pyplot as plt

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')

plt.plot([22,44,55],'--r')

plt.xlabel('Some Data')
plt.ylabel('some Other Data')
plt.title('A title')

plt.legend(['Baseline', 'Competition', 'Us'])

plt.gca().fill_between(range(len(linear_data)),
                       linear_data,
                       quadratic_data,
                       facecolor='blue',
                       alpha=0.25)

plt.show()