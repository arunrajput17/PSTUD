# To get currenty date and time we need to use datetime library

from datetime import datetime

# the now function will return the current date and time
today = datetime.now()

# Use day, month, year, hour, minute, second functions
# to display only part of the date
# All these functions return integers
# Covert them to strings before concatenating them to another string

print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))