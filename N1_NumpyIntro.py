### Numpy : Its most useful feture is n dimensional array object (a.k.a ndarray)
### Benefits of Numpy array over a python list:
### 1. Less memory, 2. Fast, 3. Convenient

import numpy as np
import time
import sys


# To create an array object use
a = np.array([1,2,3])

print(a)
print(a[0])
print(a[1])

## Comparing Python list with numpy array memory:

l = range(1000)     #python list which has 1000 elements. 1 element = 14 bytes
print(sys.getsizeof(5)*len(l))    #print the size of the list

array = np.arange(1000) # Numpy array with elements 0 to 999. 1 element = 4 bytes
print(array.size * array.itemsize)  #Print the size of array

### Fast and convenient comparison

SIZE = 1000000

#creating two list
l1= range(SIZE)
l2 = range(SIZE)

# two numpy  array
a1 =np.arange(SIZE)
a2 = np.arange(SIZE)

# measuring the time between list and numpy processing

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]  # it will take first element from l1 and l2 add them together and put them in result
print('python list took : ', (time.time()-start)* 1000)

## numpy array
start= time.time()
result = a1+a2      # convenient to add two list easily
print('numpy took : ', (time.time()-start)*1000)

## Convinient
b1 = np.array([1,2,3])
b2 = np.array([4,5,6])

print(b1+b2)
print(b2-b1)
print(b1*b2)
print(b1/b2)

