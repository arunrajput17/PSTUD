#### Handle Missing Data : replace function

import pandas as pd
import numpy as np

df = pd.read_csv('ReadWriteFiles\\P6_weather_data.csv')
print(df)

# Replace -99999 values with NAN
print('\n First ')
new_df = df.replace(-99999, np.NAN)
print(new_df)

# If we have two spcial values -99999 & -88888 then we can define them in list to replace
print('\n Second ')
new_df = df.replace([-99999,-88888],np.NAN)
print(new_df)

# Replace value based on specific column using dictionary
print('\n Third ')
new_df = df.replace({
    'temperature': -99999,
    'windspeed': [-99999,-88888],
    'Events': '0',
},np.NAN)
print(new_df)

# Replace No event with sunny and -99999 with NAN
print('\n Fourth ')
new_df = df.replace({
    -99999: np.NAN,
    'No Event': 'Sunny'
})
print(new_df)

# Regex is used to handle F,C & mph
print('\n Fifth ')
new_df = df.replace('[A-Za-z]','',regex=True)       #it replace all columns having alphabet
print(new_df)

# Using Regex based on column using dictionary
print('\n Six')
new_df = df.replace({
    'temperature': '[A-Za-z]',
    'windspeed': '[A-Za-z]'
},'',regex=True)
print(new_df)

# Replacing a list of values with another list of values
print('\n seven')
df = pd.DataFrame({
    'score': ['exceptional','average','good','poor','average','exceptional'],
    'student': ['rob','maya','parthiv','tom','julian','erica']
})
print(df)

new_df =df.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(new_df)


