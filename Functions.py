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




#################################################################

## Function is a block of code that performs a specific task
## Functions makes your code more modular and more readable.

## Problem : You are given two lists of numbers and you need to find total of each of these list

def calculate_total(exp):
    total=0
    for item in exp:
        total =total+item
    return total


tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

toms_total= calculate_total(tom_exp_list)
joes_total= calculate_total(joe_exp_list)

print("Tom's total expenses:",toms_total)
print("Joe's total expenses:", joes_total)

def sum(a,b=0): ## b = 0 is assigned as default value
    '''
    This function takes two arguments which are integer numbers and
    it will return sum of them as an output
    '''
    print('a:',a)
    print('b:',b)
    total=a+b
    print('Total inside function:',total)
    return total

n=sum(5,6)
print('Total outside function:',n)

n=sum(19)
print('Total outside function:',n)


## Write a function called calculate_area that takes base and height as an input arguments and
## returns as area of a triangle as an output . Here is the equation for an area of a triangle,
## Triangle Area = 1/2*(base * height)

def calculate_area(base, height):
    Triangle_area = 1/2 * (base * height)
    return Triangle_area

Tri_area = calculate_area(3,3)
print('Area of the triangle is:',Tri_area)


## Modify above function to take third parameter called shape type. Shape type could be either
## triangle or rectangle. Based on shape type it should calculate area. Equation for rectangle's area is,
## Rectangle Area = length * width

def calculate_area1(width, length, shape):
    if shape == 'triangle':
        Triangle_area = 1/2 * (width * length)
        return Triangle_area
    elif shape== 'rectangle':
        Rectangle_area = (width * length)
        return Rectangle_area
    else:
        print('Unknown shape type')

Tri_area1 = calculate_area1(4,4,'triangle')
print('Area of the triangle is:',Tri_area1)

Rec_area1 = calculate_area1(4,4,'rectangle')
print('Rectangle area is:',Rec_area1)

Unk_area = calculate_area1(5,5,'xyz')


## Write a function called print_pattern that takes integer number as argument and prints
## following pattern if input number is 3,
## * /n ** /n *** and If input is 4 then it should print, * /n ** /n *** /n ****

def print_pattern(num):
    for i in range(0,num):
        for j in range (0,i+1):
            print('*',end=' ')
        print()


print_pattern(3)
print() 
# print_pattern(4)

## Reverse pattern

def print_rev_pattern(num):
    for i in range (num,0,-1):
        for j in range(0, i):
            print('*',end=' ')
        print()


print_rev_pattern (4)
print()


def print_revtriangle_pattern(num):
    for i in range (num,0,-1):
        for j in range(0, num-i):
            print(end=' ')
        for k in range (0,i):
            print('*',end=' ')
        print()


print_revtriangle_pattern (4)
print()

def print_triangle_pattern(num):
    for i in range (0,num):
        # print('*',end=' ')
        for _j in range (0,num-i):
            print(end=' ')
        for _k in range (0,i+1):
            print('*',end=' ')
        print()

print_triangle_pattern(4)
print()

