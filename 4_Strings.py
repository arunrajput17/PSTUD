## Strings can be stored in variables

first_name = 'Christopher'
last_name = 'Harrison'
print(first_name+last_name)
print('Hello '+ first_name +' '+ last_name)


## Use of functions to modify strings

sentence = 'the dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))


##The functions help us format strings we save to files and databases, or display to users

first_name = input('What is your first name? ')
last_name = input('What is your last name ')

print ('Hello ' + first_name.capitalize() + ' '+ last_name.capitalize())



## Custom string formatting

output = 'Hello 1, ' + first_name + ' '+ last_name
print(output)
output = 'Hello 2, {} {}' .format(first_name,last_name)
print(output)
output = 'Hello 3, {0}, {1}'.format(first_name,last_name)
print(output)
# Only availble in Python 3
output= f'Hello format, {first_name} {last_name}'
print(output)



#######################################

#Access string vaue by index
text='ice cream'
print(text[5])

print(text[0:3])
print(text[4:9])

print(text[:3])
print(text[4:])

t1= 'Earth revolves around the sun'
print(t1[6:14])
print(t1[-3:])

# Save multiline in string

address='''add line1 
add line2'''

print(address)

print(address.encode())