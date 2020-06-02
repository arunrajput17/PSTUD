## Stack Unstack dataframe reshaping technique

import pandas as pd

df = pd.read_excel('ReadWriteFiles\\P12_stocks_data.xlsx',header=[0,1])
print(df)
print()

# Second header to row names
df1 = df.stack()
print(df1)
print()

# First header to row names
df2=df.stack(level=0)
print(df2)
print()

# reverse action using unstack
df3=df1.unstack()
print(df3)
print()


############# 3 headers

df4 = pd.read_excel('ReadWriteFiles\\P12-1_stocks_data.xlsx',header=[0,1,2])
print(df4)
print()


df5 = df4.stack()
print(df5)

