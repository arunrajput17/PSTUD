#### Merge Dataframes

import pandas as pd

df1 =pd.DataFrame({
    'city': ['new york','chicago','orlando'],
    'temperature': [21,14,35],
})
print(df1)


df2 =pd.DataFrame({
    'city': ['chicago','new york','orlando'],
    'humidity': [65,68,75],
})
print(df2)

# Merging two dataframes
df3= pd.merge(df1,df2,on='city')
print(df3)

# Only the common in both dataframe will display
df4 =pd.DataFrame({
    'city': ['new york','chicago','orlando','baltimore'],
    'temperature': [21,14,35,32],
})
print(df4)


df5 =pd.DataFrame({
    'city': ['chicago','new york','san fransisco'],
    'humidity': [65,68,71],
})
print(df5)

df6 = pd.merge(df4,df5,on='city')
print(df6)

## Union of these two dataframe tables

df7 = pd.merge(df4,df5,on='city',how='outer')
print(df7)

## Other joins
df8 = pd.merge(df4,df5,on='city',how='right')
print(df8)

df9 = pd.merge(df4,df5,on='city',how='left')
print(df9)

## We can add indicator to know which value came from which dataframe
df10 = pd.merge(df4,df5,on='city',how='outer',indicator=True)
print(df10)

## Both dataframes have same column names

df11 =pd.DataFrame({
    'city': ['new york','chicago','orlando','baltimore'],
    'temperature': [21,14,35,38],
    'humidity':[65,68,71,75]
})
print(df11)

df12 =pd.DataFrame({
    'city': ['chicago','new york','san diego'],
    'temperature': [21,14,35],
    'humidity':[65,68,71]
})
print(df12)

df13= pd.merge(df11,df12,on='city')
print(df13)

df14 = pd.merge(df11,df12,on='city',suffixes=('_left','_right'))
print(df14)