### Read database records into pandas dataframe and write it back

import pandas as pd
import sqlalchemy

# Creating sqlalchemy engine
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')

df = pd.read_sql_table('customers',engine)

# Reading few columns
df = pd.read_sql_table('customers',engine, columns=['name'])

# writing query to fetch data using join
query='''
select customers.name, customers.phone_number, orders.name, orders.amount
from customers Inner join orders
on customers.id = orders.customer_id
'''

df = pd.read_sql_query(query,engine)


# Write data in database from csv
df = pd.read_csv('customers.csv')
print(df)

## renaming column name to match with database table columns name
df.rename(columns={
    'customer name' : 'name',
    'customer phone': 'phone_number'
}, inplace=True)
print(df)

# writing in database
df.to_sql(
    name='customers',
    con=engine,
    index= False,
    if_exists='append'
)



pd.read_sql(query,engine)