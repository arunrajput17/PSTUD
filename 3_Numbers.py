## Working with numbers

# Numbers can be stored in variables
pi = 3.14159
print(pi)

# Math with numbers
first_num = 6
second_num = 2
print(first_num + second_num) # Addition
print(first_num - second_num) # Subtraction
print(first_num * second_num) # Multiplication
print(first_num / second_num) # Division
print(first_num ** second_num) # Exponent

# If you combine strings with numbers, Python get confused
days_in_feb = 29
# print(days_in_feb + 'days in February') #this is the confused example
print(str(days_in_feb)+ ' days in February')


#Numbers can be stored as strings
#Numbers stored as strings are treated as strings

first_num ='5'
second_num = '6'
print(first_num + second_num)

# The input function always returs string
first_num = input('Enter first number :')
second_num = input('Enter second number :')
print(first_num + second_num) #it will return string
print(int(first_num) + int(second_num)) #it will return integer
print(float(first_num) + float(second_num)) #it will return decimal

