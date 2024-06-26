import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('files/fifa_data.csv')

##################### HISTOGRAM ###########################
'''
bins = [30, 40, 50, 60, 70, 80, 90, 100]


plt.hist(fifa.Overall, bins=bins, color='#abcdef')
plt.xticks(bins)

plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distrubution of Player Skills in FIFA 2018')

'''
########################### Pie Charts #####################################
'''
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
print(left, right)

labels = ['Left', 'Right']
colors = ['first color', 'second color']


plt.pie([left, right], labels=labels, autopct='%.2f %%')
plt.title('Foot Preference of FIFA PLayers')
'''
########################## Pie Chart 2 ######################################
fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

plt.style.use('ggplot')

light = fifa.loc[(fifa.Weight < 125)].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa.loc[(fifa.Weight > 200)].count()[0]

weights = [light, light_medium, medium_heavy, heavy]
#explode = (.1, .1, .1, .1, .1)
#labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']





plt.pie(weights, autopct='%.2f%%') #  labels=labels explode=explode
plt.title('Weight Distribution of FIFA Players (lbs)')
#plt.legend()
#print(fifa)
plt.show()