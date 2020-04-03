import json

# create a dictionary object
person_dict = {'first': 'Christopher', 'last': 'Harrison'}

# Add dictionary key pairs to dictionary as needed
person_dict['city']='Seattle'

#convert dictionary to json object
person_json = json.dumps(person_dict)


#print JSON object
print(person_json)

###### Create JSON with nested dictionary#########

#Create a staff dictionary 
#assign a person to a staff posiyion of program manager
staff_dict={}
staff_dict['Program Manager']= person_dict

staff_json = json.dumps(staff_dict)

print(staff_json)


##################################################################

## JSON = Java Script Object Notation
## JSON is a data exchange format similar to XML

book= {}

book['tom']= {
    'name':'tom',
    'address': '1 red street, NY',
    'phone':7655667565
}


book['bob']= {
    'name':'bob',
    'address': '1 greenred street, NY',
    'phone':6467577582
}

import json

s=json.dumps(book)   # Converting dictionary into JSON 
print('JSON Print')
print(type(s))
print(s)

with open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\book.txt','w') as f:
    f.write(s)      # writing JSON into text file


with open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\book.txt','r') as fin:
    d= fin.read()   #Reading JSON file and saving it into String
    print('print 2')
    print(type(d))
    print(d)

book2 =json.loads(d)        # Converting string into Dictionary
print('print3')
print(type(book2))
print(book2)

print(book2['bob'])     # Printing values of bob from Dictionary
print(book2['bob']['phone'])        # printing particular value of bob from dictionary


for person in book2:        # Accessing all the values in the dictionary
    print(book[person])