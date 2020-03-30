#Lists are collections of item (Lists can have data of any type)

names = ['Susan','Christopher' ]

print(len(names))  #Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)

search = 'Susan'in names  ## Search the value is availble in the list or not, it will return True/False
print(search)

scores = []
scores.append(98)  #Add new item to the end
scores.append(99)

## scores.remove(99)  # this is used to remove item from list
scores.append('hi')
print(scores)
print(scores[1])  # Collections are zero-indexed

# Retrieving Ranges

names = ['Susan' , 'Christopher' , 'Bill' , 'Justin']
presenters = names[1:3] #Start and End index
print(names)
print(presenters)


# Arrays are also collection of item(Arrays will have data of same type)
from array import array

scores = array('d')
scores.append(12)
scores.append(14)
print(scores)
print(scores[1])


# Dictionaries

person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])


christopher = {}
christopher['first'] = 'Christopher'
christopher['last'] = 'Harrison'

susan = {}
susan['first']  = 'Susan'
susan['last'] = 'Ibach'

people = []
people.append(christopher)
people.append(susan)
people.append({'first':'Bill', 'last' : 'Gates'})

print(people)



###############################################################################

## Dictionary allows to store key , value pair
## They are also known as, Maps, Hashtables, Associate Arrays

d={'tom':7320923203,'rob':7325730239,'joe':732092320}
print(d)
print(d['tom'])

##Adding entry
d['sam']=7395679879
d['bob']=5757575757
print(d)

## Deleting entry
del d['sam']
print(d)

##How to print all the directory values

for key in d:
    print('key:',key,'value:',d[key])

#another way to print all values in Dictionary is by using Tuples

for k,v in d.items():
    print('key:',k,'values',v)

## Search particular key in Dictionary
print ('tom' in d)
print('samir' in d)

## To clear all the dictionary item
d.clear()
print(d)

## TUPLES : Tuples is a group of values grouped together
## List: All values have similar meaning(Homogenous)
## Tuple: All values have different meaning (heterogenous)
## Tuple example

point=(4,5)  # 4 is x coordinate , 5 is y coordinate
address = ('1 purple street','new york',10001)

print(point[0])

## Tuples are immutable
# point[0] = 50

## Write a python program that allows to store age of your family members. Program should ask to enter
## person name and age and once you are done you should be able to input name of the person and program
## should tell the age. Now print name of all your family members along with their ages.

Number_of_family_members = int(input('Enter number of family number:'))

name_age_Dict={} ## Initializing the dictionary

for i in range (0,Number_of_family_members):  ## Entering data in dictionary
    name = input('Enter Name: ')
    age = input('Enter Age:')
    name_age_Dict[name]=age
    # print(name_age_Dict)

find_age_by_name = input('Enter name to find age of the person:') #Entering name of the person to find age

for j in name_age_Dict: ## Finding age of the person
    if j == find_age_by_name:
        print('Age of ',j, 'is',name_age_Dict[j])


for k in name_age_Dict: # printing all the dictionary items
    print('Name:',k,'Age:',name_age_Dict[k])

############################      OR ########################

def age_dictionary():
    d={}

    while True:
        person = input('Enter person name, to stop dont enter anything and hit enter:')
        if person=='':
            break
        age= input('Enter Age:')
        d[person]=age
    
    print('Now Enter the name and i will tell you his/her age')

    while True:
        name=  input('Enter person name, to stop dont enter anything and hit enter:')
        if name=='':
            break
        if name in d:
            print('Age of',name, 'is',d[name])
        else:
            print('I dont know the age of',name)
    print('Age dictionary program is finished')


age_dictionary()
    


## Write a function called add_and_multiply that takes two numbers as input and it should return sum and 
## multiplication as two separate numbers.

def add_and_multiply (a,b):
    sum= a+b
    mult = a*b
    return sum, mult

a=4
b=5
s,m=add_and_multiply(a,b)
print('sum:',s,'Multiplication',m,'Input numbers:', a, 'and', b)


