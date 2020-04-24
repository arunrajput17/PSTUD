## Diferent ways of creating dataframe,

import pandas as pd


# 1. Using CSV
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\weather_data.csv')
print(df)

# 2. Using Excel
df = pd.read_excel('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\weather_data.xls','Sheet1')
print(df)

df = pd.read_excel('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\weather_data.xlsx','Sheet1')
print(df)


# 3. From python dictionary

weather_data1 ={
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,32],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain','Sunny','Snow','Snow','Rain','Sunny']
}

df = pd.DataFrame(weather_data1)
print('Dataframe created from dictionary : \n', df)


# 4. From list tuples

weather_data2 =[
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]

df = pd.DataFrame(weather_data2, columns=['day','temperature','windspeed','event'])
print('Dataframe created from tuples: \n',df)

    

# 5. From list dictionaries 

weather_data3 =[
    {'day':'1/1/2017','temperature':32,'windspeed':6,'event':'Rain'},
    {'day':'1/2/2017','temperature':35,'windspeed':7,'event':'Sunny'},
    {'day':'1/3/2017','temperature':28,'windspeed':2,'event':'Snow'},
]

df = pd.DataFrame(weather_data3)
print('Dataframe created from list dictionaries : \n',df)
