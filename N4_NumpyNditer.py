## Iterate numpy array using nditer

import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

# iterating using for loop for row
for row in a:
    print(row)

# iterating over each of element one by one then
for row in a:
    for cell in row:
        print(cell)

# flaten this array into list
for cell in a.flatten():
    print(cell)
print()

# nditer allow more sophisticated way of iteration

for x in np.nditer(a,order='C'):        
    print(x)
print()

for x in np.nditer(a,order='F'):        # fortan order
    print(x)

# Print entire column on each iteration
for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)


# Using opflags we can readwrite the original array

a1=np.arange(12).reshape(3,4)
print(a1)

for x in np.nditer(a1,op_flags=['readwrite']):
    x[...]=x*x
print(a1)        # print the original array values square


# How to iterate through two numpy arrays simultaneously
# they are compatible when either they are of equal shape or one of them is one

b = np.arange(3,15,4).reshape(3,1)
print(b)
print()

for x,y in np.nditer([a1,b]):
    print(x,y)




