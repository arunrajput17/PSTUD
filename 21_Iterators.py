## Iterators :

a =['hey','bro','you are','awesome']

for i in a:
    print (i)

print(dir(a))
itr = iter(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))



# List
for element in [1,2,3]:
    print(element)

# Tuple
for element in (1,2,3):
    print(element)

# Dictionary keys
for key in {'one':1,'two':2}:
    print(key)

# Characters in the string
for char in '123':
    print(char)

# Every line in a file
for line in open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny1.txt'):
    print(line,end='')

print()

# Remote control

class RemoteControl():
    def __init__(self):
        self.channels = ['HBO','CNN','abc','espn']
        self.index = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))



