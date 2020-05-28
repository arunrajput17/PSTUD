## melt is used to transform or reshape data

import pandas as pd

df = pd.read_csv('ReadWriteFiles\\P11_weather_data_ByCities.csv')
print(df)

# covert data citiwise
df1 = pd.melt(df,id_vars=['Day'])
print(df1)

# filter on chicago
df2=df1[df1['variable']=='chicago']
print(df2)

# Defining column names
df3= pd.melt(df,id_vars='Day',var_name='city',value_name='temperature')
print(df3)

