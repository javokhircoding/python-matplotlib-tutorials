import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = [0, 1, 3, 5, 6, 6, 7]
y = [0, 1, 2, 3, 3, 4, 6]

## Resizing the graph
plt.figure(figsize=(5, 3), dpi=100)  #figsize - size of graphic, dpi - pixels



## Drawing line
# plt.plot(x, y, label='2x', color='purple', linewidth=3, marker='.', linestyle='solid', markersize=13, markeredgecolor='black')    # plot() is the easiest way to draw graphics | It shows just a line
# but we have some better way
## Shordhand notation
# '[color][marker][line]'
plt.plot(x, y, 'r.-', label='2x')

## 2nd line
x2 = np.arange(0,4.5,0.5)
#plot square
plt.plot(x2[:5], x2[:5]**2, label='x^2', marker='.', color='purple')
plt.plot(x2[4:], x2[4:]**2, label='x^2', marker='.', linestyle='--', color='purple')







## Adding a label
plt.xlabel('X axis')
plt.ylabel('Y axis')

## Title
plt.title('Our first graph | Just a line', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})  #sets the title of figure

## Changing the ticks
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0, 2, 4, 6, 8, 10])

## Legend
plt.legend()


## to sace the graph
plt.savefig('graph/mygraph.png', dpi=300)

## Showing the figure
plt.show()  #to show the graphic in any terminal you must use .show() method


