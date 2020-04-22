## Numpy: Slicing / Stacking and indexing with boolean arrays

import numpy as np

#Slicing
n = [6,7,8]        # Normal list
print(n[0:2])
print(n[-1])

a = np.array([6,7,8])   #Numpy array
print(a[0:2])
print(a[-1])

b = np.array([[6,7,8],[1,2,3],[9,3,2]]) #Multidimensional array
print(b)
print(b[1,2])   #accessing values by defining row & column
print(b[0:2,2])
print(b[-1])
print(b[-1,0:2])
print(b[:,1:3])

#iterate through array
for row in b:
    print(row)

# Flaten the array and print every cell
for cell in b.flat:
    print(cell)


# Stacking two arrays together
a1 = np.arange(6).reshape(3,2)
a2 = np.arange(6,12).reshape(3,2)
print(a1)
print(a2)

print(np.vstack((a1,a2)))       #Stacking them together vertically

print(np.hstack((a1,a2)))       # Stacking them together horizontally

#Horizontal split of big array into 3 equal sized array
a3= np.arange(30).reshape(2,15)
print(a3)

print(np.hsplit(a3,3))

result = np.hsplit(a3,3)
print(result[0])
print()
print(result[1])
print()
print(result[2])
print()

# Vertical spliting of big array into 2 equal sized array

vresult = np.vsplit(a3,2)
print(vresult[0])
print()
print(vresult[1])
print()


#########Indexing with boolean arrays#############

b1 = np.arange(12).reshape(3,4)

print(b1)

b2 = b1>4   # checking b1 values are greater than 4 or not and saving result in boolean form in b2 array

print(b2)

print(b1[b2])      #Here b2 array is the index of b1 array & will return value from b1 where b2 is true

b1[b2]= -1       # Replace True values with other value
print(b1)