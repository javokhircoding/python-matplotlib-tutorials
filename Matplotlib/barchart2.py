import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



labels = ['A', 'B', 'C']
values = [1, 4, 2]

bars = plt.bar(labels, values)

## Sizing
#plt.figure(figsize=(6, 4), dpi=100)

# We can give specific looking by using index
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
# or we can do easier method
patterns = ['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

## adding legend
plt.legend() #it's not necassary at this figure

plt.show()