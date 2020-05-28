### Pivot Table : it allows you to transform and reshape data

import pandas as pd

df = pd.read_csv('ReadWriteFiles\\P10_weather_data_ByCities.csv')
print(df)

# Transform it rows as index and column as cities
df1=df.pivot(index='date',columns='city')
print(df1)
print()

# Transform to see humidity only
df2= df.pivot(index='date',columns='city',values='humidity')
print(df2)
print()

# humidity as rows columns are city
df3= df.pivot(index='humidity',columns='city')
print(df3)
print()


#### Pivot table is used to summarize and aggregate data inside dataframe

df=pd.read_csv('ReadWriteFiles\\P10-1_weather_data_ByCities.csv')
print(df)
print()

## Average temp through out the day
df4=df.pivot_table(index='city',columns='date')
print(df4)
print()

## Aggregation using sum, mean, count, div
df5 = df.pivot_table(index='city',columns='date',aggfunc='sum')
print(df5)
print()

# using mrgins
df6 = df.pivot_table(index='city',columns='date',margins=True)
print(df6)
print()

###Grouper in pivot -- Average temp in may
df=pd.read_csv('ReadWriteFiles\\P10-2_weather_data_ByCities.csv')
print(df)
df['date']=pd.to_datetime(df['date'])
df7= df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')
print(df7)


