#Sometimes we copy and paste our codes

import datetime
#print timestamps to see how long sections of code take to run

first_name = 'Susan'
print ('task completed')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print ('Task completed 2')
print (datetime.datetime.now())
print()

##############################################
## Use functions instead of repeating code

#print the current time
def print_time():
    print('Task completed 3')
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
print_time()


#############################################
#pass the task name as a parameter
def print_time1(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time1('First name assigned')

for x in range(0,10):
    print(x)
print_time1('loop completed')


##############################################
##Another example where code looks different but we are doing the same logic over and over

first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]

last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are :' + first_name_initial + last_name_initial)

##I can still use a function but this time my function return value
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your initials are :' + get_initial(first_name) + get_initial(last_name))





