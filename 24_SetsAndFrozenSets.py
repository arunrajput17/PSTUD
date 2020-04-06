## Set : Set is an unordered collection of unique elements

basket ={'orange','apple','mango','apple','orange'}
print(type(basket))
print(basket)

# other way to initialize set
a=set()
a.add(1)
a.add(2)

print(a)

# Do not initialize with empty {} brackets otherwise it will be initialized as dictionary
# if some content in it thn it is initialized as set

b={}
print(type(b))

b={'something'}
print(type(b))

## List allow index operation but set doesn't allow
# print(basket[0])


## removing duplicate elements from list

numbers=[1,2,3,4,2,3,4]
unique_numbers = set(numbers)  #list to sets
print(unique_numbers)

unique_numbers.add(5)
print(unique_numbers)

set_to_list_unique_numbers = list(unique_numbers) # set to list
print(set_to_list_unique_numbers)


# set to be frozen i.e. not able to change the content of set
fs = frozenset(numbers)
print(fs)

# fs.add(5)  # it will not allow to add in frozen set

### basic operation of set

x={'a','b','c'}
print('a' in x)
print('g'in x)

for i in x:
    print(i)

y={'a','g','h'}

print(y)

# Union
print(x|y)

# intersection
print(x&y)

# difference
print(x-y)

# sub set to check x is subset of y
print(x<y)

# after changing
x={'h','g'}
print(x)
print(x<y)

