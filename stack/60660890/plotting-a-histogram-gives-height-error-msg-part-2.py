import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

xaxis=['epic1', 'epic2', 'epic3', 'epic4', 'epic5', 'epic6','epic7']
n=len(xaxis)
names = ('epic1', 'epic2', 'epic3', 'epic4', 'epic5', 'epic6','epic7')
data = {'done': [57,53,49,65,78,56,89], 'progress': [23,12,34,11,34,12,12], 'todo' :[11,5,6,7,8,4,6]}

df = pd.DataFrame(data)
df['total'] = df['done'] + df['progress'] + df['todo']

df['done_per'] = df['done'] / df['total'] * 100
df['progress_per'] = df['progress'] / df['total'] * 100
df['todo_per'] = df['todo'] / df['total'] * 100

done_per = df['done_per']
progress_per = df['progress_per']
todo_per = df['todo_per']

barWidth = 0.25
# Create green Bars
plt.bar(xaxis, done_per, color='#b5ffb9', edgecolor='white', width=barWidth)
# Create orange Bars
plt.bar(xaxis, progress_per, bottom=done_per, color='#f9bc86', edgecolor='white', width=barWidth)
# Create blue Bars
plt.bar(xaxis, todo_per, bottom=[i+j for i,j in zip(done_per, progress_per)], color='#a3acff', edgecolor='white', width=barWidth)

# Custom x axis
plt.xticks(xaxis, names)
plt.xlabel("epics")

# Show graphic
plt.show()