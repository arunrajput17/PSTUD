## We often need current date and time when logging errors and saving data

# To get date and time we need to use the datetime library
from datetime import datetime

current_datetime = datetime.now() #the now function returns a datetime object
print('Today is: ' + str(current_datetime))


# There are functions you can use with datetime objects to manipulate dates
from datetime import datetime, timedelta
today = datetime.now()
print('Today is : '+ str(today))

# timedelta is used to define a period of time
one_day = timedelta(days = 1)
yesterday = today - one_day
print ('Yesterday was :' + str(yesterday))

one_week = timedelta(weeks= 1)
last_week = today - one_week
print('Last week was:' + str(last_week))