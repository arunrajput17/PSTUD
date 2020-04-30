##### Group By (Split Apply combine)

import pandas as pd

df = pd.read_csv('ReadWriteFiles\\P7_weather_data_ByCities.csv')
print(df)

# 1. Find maximum temperature in each of cities
print('\n First ')

g = df.groupby('city')
print(g)

print('\n second ')
# how to Access each of these groups
for city, city_df in g:
    print(city)
    print(city_df)

print('\n third ')
# access a specific  dataframe
print (g.get_group('mumbai'))

print('\n Fourth ')
# print(g['temperature'].max())
print(g.max())

# 2. Find average wind speed per city

print(g.mean())
print(g.describe())

import matplotlib.pyplot as plt

# %matplotlib inline
print(g.plot())
plt.show()




