import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random import shuffle


origins = ['China', 'Brazil', 'India', 'USA', 'Canada', 'UK', 'Germany', 'Iraq', 'Chile', 'Mexico']

shuffle(origins)

df = pd.DataFrame({'height': np.random.rand(10),
                   'weight': np.random.rand(10),
                   'origin': origins})

plt.figure()
plt.ion()
plt.scatter(df['height'], df['weight'], picker=5)
plt.gca().set_xlabel('Height')
plt.gca().set_ylabel('Weight')

def onpick(event):
    origin = df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('Selected item came from {}'.format(origin))


plt.gcf().canvas.mpl_connect('pick_event', onpick)

plt.show()