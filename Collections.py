#Lists are collections of item (Lists can have data of any type)

names = ['Susan','Christopher' ]

print(len(names))  #Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)


scores = []
scores.append(98)  #Add new item to the end
scores.append(99)
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