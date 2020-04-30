#### Concat Dataframes

import pandas as pd

india_weather =pd.DataFrame({
    'city': ['mumbai','delhi','banglore'],
    'temperature': [32,45,30],
    'humidity':[80,60,78]
})

print(india_weather)

us_weather =pd.DataFrame({
    'city': ['new york','chicago','orlando'],
    'temperature': [23,14,35],
    'humidity':[68,65,75]
})
print(us_weather)

#concating two df into one but showing existing index numbers
df= pd.concat([india_weather,us_weather])
print(df)

# concating two dataframes with continuos index

df = pd.concat([india_weather,us_weather], ignore_index=True)
print(df)

# Passing keys for two dataframes for fetching records as per key
df = pd.concat([india_weather,us_weather],keys=['india','us'])
print(df)
print(df.loc['india'])

#Appending two dataframes as column
temperature_df =pd.DataFrame({
    'city': ['mumbai','delhi','banglore'],
    'temperature': [32,45,30],
})

windspeed_df =pd.DataFrame({
    'city': ['delhi','mumbai'],
    'windspeed': [7,12],
})

df = pd.concat([temperature_df,windspeed_df],axis=1)    #it was not concating correctly delhi with delhi
print(df)

# assigning index  to solve above issue
temperature_df =pd.DataFrame({
    'city': ['mumbai','delhi','banglore'],
    'temperature': [32,45,30],
},index=(0,1,2))

windspeed_df =pd.DataFrame({
    'city': ['delhi','mumbai'],
    'windspeed': [7,12],
},index=(1,0))

df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)


# joining dataframe with series
print(temperature_df)

s = pd.Series(['Humid','Dry','Rain'],name='event')
print(s)

df=pd.concat([temperature_df,s],axis=1) #appending series in dataframe
print(df)

