## Pandas

import pandas as pd

df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\nyc_weather.csv')

print(df)

# What is max temperature
print(df['Temperature'].max())

# To know on which dates it rains
print(df['EST'][df['Events']=='Rain'])

# To get average windspeed

# print(df['WindSpeedMPH'])
print(df['WindSpeedMPH'].mean())

# Process of cleaning messy data is called data munging or data wrangling
df.fillna(0,inplace=True)
# print(df['WindSpeedMPH'])
print(df['WindSpeedMPH'].mean())


