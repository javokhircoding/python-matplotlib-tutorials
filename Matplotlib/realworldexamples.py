import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('files/gas_prices.csv')


plt.figure(figsize=(10, 5))  # fontdict={'bold': 'Comic Sans MS', 'fontsize': 20}
plt.title('Gas Prices(1990-2008)')


plt.plot(gas.Year, gas.USA, label='USA', marker='.')
plt.plot(gas.Year, gas.UK, label='UK', marker='.') # as an x par.. we have years, as an y par.. we have gas prices plot(x, y)
plt.plot(gas.Year, gas.Canada, label='Canada', marker='.')
plt.plot(gas.Year, gas.Japan, label='Japan', marker='.')
plt.plot(gas.Year, gas.Australia, label='Australia', marker='.')
plt.plot(gas.Year, gas.Germany, label='Germany', marker='.')
plt.plot(gas.Year, gas.Mexico, label='Mexico', marker='.')
plt.plot(gas.Year, gas.Italy, label='Italy', marker='.')
plt.plot(gas.Year, gas['South Korea'], label='South Korea', marker='.')


### Eeeeasiest way

'''
for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], label=, marker='.')
        '''

plt.xticks(gas.Year[::2])
plt.xlabel('Year')
plt.ylabel('Prices(USD)')


print(gas)
plt.legend()
plt.savefig('graph/gas_prices.jpg')
plt.show()
