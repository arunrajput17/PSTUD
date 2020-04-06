## Generators : It is a simple way of creating iterator.

def remote_control_next():
    yield 'cnn'
    yield 'espn'


itr = remote_control_next()
print(itr)
print(next(itr))
print(next(itr))
# print(next(itr))



for c in remote_control_next():
    print(c)


## Fibonacci seqence (0,1,1,2,3,5,8,13,.....)
# Produce using generators

def fib():
    a, b = 0, 1
    while True:
        yield a
        a,b = b , a+b

for f in fib():
    if f > 50:
        break
    print(f)

### Benefits of using generators over class based iterator
# 1. You dont need to define iter() and next() methods
# 2. You dont need to raise StopIteration exception





