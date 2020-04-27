## Handle Missing Data : fillna, dropna, interpolate

# 1. fillna to fill missing values using different ways
# 2. interpolate to make a guess on missing values using interpolation
# 3. dropna to drop rows with missing values

import pandas as pd

df = pd.read_csv('ReadWriteFiles\\P5_weather_data.csv')
print(df)

print(type(df.day[0]))  # Check the type of column

# Convert day column str into date 
df = pd.read_csv('ReadWriteFiles\\P5_weather_data.csv', parse_dates=['day'])
print(type(df.day[0])) # Format changed to Time stamp

df.set_index('day', inplace = True) # setting day as index value
print(df)

################### Fillna #########################

new_df=df.fillna(0) # replacing blank value with 0
print(new_df)

#replacing na with different values for columns
new_df = df.fillna({   
    'temperature': 0,
    'windspeed': 0,
    'Events': 'no event'
})

print(new_df)

## inplace of NAN we are filling previous day value
new_df = df.fillna(method='ffill')
print(new_df)

## inplace of NAN we are filling next day value
new_df = df.fillna(method='bfill')
print(new_df)

## replacing NAN values with next column data
new_df = df.fillna(method='bfill',axis='columns')
print(new_df)


# LImit can be added to replace values upto what number of cell
new_df = df.fillna(method='ffill',limit=1)
print(new_df)



############################ Interpolate ######################

## inplace of NAN we are guessing values linearly between previous and next day
new_df = df.interpolate()
print(new_df)

## inplace of NAN we are guessing values based on time between previous and next day
new_df = df.interpolate(method='time')
print(new_df)


############################ Dropna ######################

## Drop all the rows with NA value. If any row contain NA then it will drop that row
new_df = df.dropna()
print(new_df)

## Drop only if all are NA
new_df = df.dropna(how='all')
print(new_df)

## keep only those rows which has at least one non NA value
new_df = df.dropna(thresh=1)
print(new_df)

## keep only those rows which has at least two non NA value
new_df = df.dropna(thresh=2)
print(new_df)



## How do you insert the missing days

dt = pd.date_range('01-01-2017','01-11-2017')
idx = pd.DatetimeIndex(dt)
df=df.reindex(idx)

print(df)