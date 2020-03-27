print('Hello World single quotes')
print("Hello world double quotes")
print()
print('Did you see the blank line?')
print('Blank line \nin the middle of the string')
print("It's a small world after all.")

name = input('Please enter your name: ')
print(name)
print()

# Debbugging with print
print('Adding numbers')
x= 42 + 206
print('Performing division')
y= x/1
print('Math complete')



# name= input('Enter your name ')
# print ('hello python '+ name)

x=5
print('i am integer '+ str (x))


###############################

var1= 1
var2 =2
var3 = 3
print(var1,var2,var3)

## Using sep keyword in python print
print(var1,var2,var3,sep='_')
print(var1,var2,var3,sep='separator')

####### Using end keyword in print

initList = ['camel', 'case', 'stop']

# print each words using loop
print('Printing using default print function')
for item in initList:
    print(item)  # default print function. newline is appended after each item.

print()  # another newline

# print each words using modified print function
print('Printing using modified print function')
for item in initList:
    print(item, end='-')

##### file keyword in print

# open a file in writable mood
fi = open('output.txt', 'w')

# initialize a list
initList = ['Lion', 'case', 'stop']

# print each words using loop
print('Printing using default print function')
for item in initList:
    print(item, file=fi)  # use file keyword

print(file=fi)

# print each words using modified print function
print('Printing using modified print function')
for item in initList:
    print(item, end='-', file=fi)  # use file keyword

# close the file
fi.close()