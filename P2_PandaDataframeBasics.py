## Dataframe basics :
## Datarame is a main object in Pandas. It is used to represent data with 
## rows and columns(tabular or excel spreadsheet like data)

import pandas as pd

# 1. Creating dataframe

# df = pd.read_csv('ReadWriteFiles\\weather_data.csv')  # If file is in folder of project then we can define this way
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\weather_data.csv')

print(df)

# We can create dataframe from python dictionary also

# weather_data ={
#     'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
#     'temperature': [32,35,28,24,32,32],
#     'windspeed': [6,7,2,7,4,2],
#     'event': ['Rain','Sunny','Snow','Snow','Rain','Sunny']
# }

# df1 = pd.DataFrame(weather_data)
# print(df1)


# 2. Dealing with rows and columns

rows, columns = df.shape    # To find number of rows and column
print('No. of rows are :', rows)
print('No. of columns are:', columns)

print(df.head())        # it is going to print initial few rows only
print(df.head(2))   # it will print only 2 rows

print(df.tail())    # it will print last 5 rows
print(df.tail(1))   # it will print last row only

print(df[2:5])      # To print only data from 2 to 4th row
print(df[:])        # To print all
print(df)           # to print all

print(df.columns)   # To print columns
print(df.day)       # To print individual column OR
print(df['Events'])  # To print individual column

print(type(df['Events']))   # to see the type

print(df[['day','Events','windspeed']])     # To print selected columns only



# 3. Operations: min, mas, std, describe

print(df['temperature'].max()) # Maximum temperature
print(df['temperature'].mean()) # Mean of temp
print(df['temperature'].min())  # Min Temp
print(df.describe())        # It gives the statistics of data



# 4. Conditional selection ( like SQL we can fetch records on conditional basis)

print(df[df.temperature>=32])   # it will give data of temp above and equal to 32

print(df[df.temperature == df.temperature.max()])   # it will print data for the max tempe row Or
print(df[df.temperature== df['temperature'].max()])

print(df['day'][df.temperature== df['temperature'].max()]) # It will print the specific day only
print(df[['day','temperature']][df.temperature== df['temperature'].max()])  # Day and temperature



# 5. set_index

print(df)
print(df.index) # give the current index of dataframe

df2 = df.set_index('day') # It returns new dataframe. it doesnt modify the existing dataframe
print(df)
print(df2)

# To modify the existing dataframe
df.set_index('day',inplace=True)
print(df)

# Now we can use date as index
print(df.loc['1/3/2017'])

# to reset the index
df.reset_index(inplace=True)
print(df)

# set event as index which is having duplicate values
df.set_index('Events',inplace=True)
print(df)
print(df.loc['Snow'])       # it wil print both the rows

df.reset_index(inplace=True)
print(df)
