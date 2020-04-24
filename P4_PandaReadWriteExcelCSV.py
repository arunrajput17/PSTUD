## Reading writing csv, excel files

import pandas as pd

############## 1. Read csv ###############
print('Reading CSV started \n')

df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\stock_data_withHeader.csv')
print(df)

# to skip the first row or header
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\stock_data_withHeader.csv',skiprows=1)
print(df)

# Also we can remove header using
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\stock_data_withHeader.csv',header=1)
print(df)


# Without header csv file then it will auto generate
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\stock_data_withoutHeader.csv',header=None)
print(df)

# Without header csv file and define them manually
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\stock_data_withoutHeader.csv',header=None, names=['ticker','eps','revenue','price','people'])
print(df)

# If file is big and we want read only few rows lets say 3 rows 
df = pd.read_csv('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\stock_data_withHeader.csv',header=1, nrows=3)
print(df)

# Want to read n.a. or not available  as NAN
df = pd.read_csv('ReadWriteFiles\\stock_data_withHeader.csv',header=1, na_values=['not available','n.a.'])
print(df)

# How to define columnwise that what data we want to convert (for that instead of list we supply dictionary)
df = pd.read_csv('ReadWriteFiles\\stock_data_withHeader.csv',header=1, na_values={
    'eps':['not available','n.a.'],
    'revenue':['not available','n.a.',-1],
    'price':['not available','n.a.'],
    'people':['not available','n.a.']
    })
print(df)

print('Reading CSV finished \n')

############### 2. Write csv ####################
print('CSV writting started \n')

# New file written with default index
df.to_csv('ReadWriteFiles\\new_written_withIndex.csv')

#new file written without Index
df.to_csv('ReadWriteFiles\\new_written_withoutIndex.csv',index=False)

# Write only selected columns
print(df.columns)
df.to_csv('ReadWriteFiles\\new_written_selectedColumsOnly.csv',columns=['tickers','eps'])

# Skipping the header while writing
df.to_csv('ReadWriteFiles\\new_written_withoutHeader.csv',header=False)

print('CSV writting finished \n')



################# 3. Read excel ###############
print('Reading xls started \n')

df = pd.read_excel('ReadWriteFiles\\stock_data_withHeader.xls','Sheet1')
print(df)


df = pd.read_excel('ReadWriteFiles\\stock_data_withSingleHeader.xls','Sheet1')
print(df)

# Conversion of cell content from excel
def convert_people_cell(cell):
    if cell == 'n.a.':
        return 'sam walton'
    return cell
def convert_eps_cell(cell):
    if cell == 'not available':
        return None
    return cell


df = pd.read_excel('ReadWriteFiles\\stock_data_withSingleHeader.xls','Sheet1',converters={
    'people' : convert_people_cell,
    'eps': convert_eps_cell
    })
print(df)

print('Reading xls finished \n')

########################## # 4. Write excel #######################
print('Writing xls started \n')

# New file written with default index
df.to_excel('ReadWriteFiles\\new_writtenExcel_withIndex.xls',sheet_name='stocks')

# New file written without default index
df.to_excel('ReadWriteFiles\\new_writtenExcel_withoutIndex.xlsx',sheet_name='stocks',index=False)

# Start Writing from particular rows column
df.to_excel('ReadWriteFiles\\new_writtenExcel_withParticularRowsColumn.xlsx',sheet_name='stocks',startrow=1,startcol=2)

# Two dataframes and writing them in excel
df_stocks = pd.DataFrame({
    'tickers':['GOOGL','WMT','MSFT'],
    'price': [845,65,64],
    'pe':[30.37,14.26,50.97],
    'eps':[27.82,4.61,2.12]
})

df_weather = pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,32],
    'event': ['Rain','Sunny','Snow','Snow','Rain','Sunny']
})

with pd.ExcelWriter('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\new_writtenExcel_CombinedStocksWeather.xlsx') as writer:
    df_stocks.to_excel(writer,sheet_name='stocks')
    df_weather.to_excel(writer,sheet_name='weather')


print('Writing xls finished \n')