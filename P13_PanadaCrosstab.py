### Crosstab

import pandas as pd

df= pd.read_excel('ReadWriteFiles\\P13_survey_data.xlsx')
print(df)


## Creating contengency table 
df1= pd.crosstab(df.Nationality,df.Handedness)
print(df1)

## With margin

df2 = pd.crosstab(df.Sex, df.Handedness, margins=True)
print(df2)

df3 = pd.crosstab(df.Sex,[df.Handedness,df.Nationality], margins=True)
print(df3)


## For percentage
df4 = pd.crosstab(df.Sex, df.Handedness, normalize='index')
print(df4)

# Average age of individuals
import numpy as np
df5 = pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)
print(df5)



