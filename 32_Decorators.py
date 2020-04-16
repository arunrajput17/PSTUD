
def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper


@logger
def sample():
    print('-- Inside sample function')

sample()


###################################################################

####  Decorators act as a wrapper for your original function
## Common uses are : 1. Logging, 2. Timing

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +' took ' + str((end-start)*1000)+ ' mil sec')
        return result
    return wrapper


@time_it
def calc_square(numbers):
    # start = time.time() ## Add the repeated code in decorator
    result= []
    for number in numbers:
        result.append(number*number)
    # end = time.time()   ## Add the repeated code in decorator
    # print('calc_square took '+ str((end-start)*1000)+ ' mil sec')   ## Add the repeated code in decorator
    return result

@time_it
def calc_cube(numbers):
    # start = time.time() ## Add the repeated code in decorator
    result = []
    for number in numbers:
        result.append(number*number*number)
    # end = time.time()   ## Add the repeated code in decorator
    # print('calc_cube took '+ str((end-start)*1000)+ ' mil sec') ## Add the repeated code in decorator
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)