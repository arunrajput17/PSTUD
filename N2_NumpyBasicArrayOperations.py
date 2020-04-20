## Basic array operation

import numpy as np

a = np.array([5,6,9])   # Creating one dimensional array
print(a)
print(a[0])             # We can access it just like list
print(a[2])
print('Dimension of array "a" is :',a.ndim)


b = np.array([[1,2],[3,4],[5,6]])    #Creating two dimensional array
print(b)
print('Dimension of array "b" is :',b.ndim)
print('Byte size of each integer element is :', b.itemsize)
print('data type is', b.dtype)


#intializing the array with different data type
c = np.array([[9,8],[7,6],[5,4]], dtype=np.float)
print(c)
print('Byte size each float element is :', c.itemsize)
print('Total number of elements in the array are :', c.size)
print('Dimention of array in rows and column is :', c.shape)
print('data type is', c.dtype)

# Initializing the array as Complex number datatype
d = np.array([[9,8],[7,6],[5,4]], dtype=np.complex)
print(d)


# Intialize array with some place holder numbers

z = np.zeros((3,4))
print(z)

o = np.ones((4,3))
print(o)

# we use range function for list which is same  as 'arange' in numpy
l = range(5)
print(l[0])
print(l[1])

m = np.arange(1,5) #Intialize array for 1 to 4
print(m)

#Step example
s = np.arange(1,5,2) # Intialize array for 1 to 4 with step up by 2
print(s)

#linspace function is used to generate numbers between start and stop values
lins = np.linspace(1,5,10)
print (lins)
print()
lins = np.linspace(1,5,5)
print (lins)
print()
lins = np.linspace(1,5,20)
print (lins)
print()

# REshaping array (They are not altering the original array but you can save it in new array)
r =np.array([[1,2],[3,4],[5,6]])
print(r)
print('Current shape of array is:',r.shape)
print('Reshape it to (2,3) :', r.reshape(2,3))
print('Reshape it to (6,1) :', r.reshape(6,1))

print('Ravel  it to one dimention :', r.ravel()) # Ravel function to flatten array and make it one dimenstional
print(r)
gh = r.ravel()
print(gh) # Capturing ravel in new array

gk= r.reshape(6,1)
print(gk) # Capturing reshape in new array
print()


## Mathematical operation in array

x = np.array([[1,2],[3,4],[5,6]])
print(x)
print('Minimum value in array : ', x.min())
print('Maximum value in array : ', x.max())
print('Sum all the numbers together : ', x.sum())

print('axis 0 denotes columns & for sum of column values : ', x.sum(axis=0))
print('axis 1 denotes eows & for sum of row values : ', x.sum(axis=1))

print('Square root ', np.sqrt(x)) # Squareroot is generic function not individual element function

print('Standard deviation : ',np.std(x))


### Basic mathematical operations
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print('Sum of two arrays : ', x+y)
print('Multiplication of two arrays : ', x*y)
print('Division of two arrays : ', x/y)
print('Matrix product of two arrays : ', x.dot(y))

