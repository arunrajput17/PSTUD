
x = 42
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by Zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
print()



## Exceptions : Exceptions are errors detected at the time of program execution

x=input('Enter number 1:')
y=input('Enter number 2:')

try:
    z=int(x)/int(y)
except Exception as e:
    print('Exception occured: ',e)
    z= None
except Exception as e:
    print('Excetion occured 2',type(e).__name__)
    z=None
print('Division is:',z)


############################
## Raise builtin exception

try:
    raise MemoryError('Memory Error')
except MemoryError as e:
    print(e)


try:
    raise Exception('memory error')
except Exception as e:
    print(e)


## Raise user defined exception

class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def print_exception(self):
        print('User defined exception: ',self.msg)

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.print_exception()


## Finally: If exception happens and there is no handling of the exception 
## in except block still it will execute finally block.

def process_file():
    try:
        # f=open('c:\\code\\data.txt')
        f=open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny1.txt')
        x=1/0
    except FileNotFoundError as e:
        print('inside except')
    finally:
        print('cleaning up file')
        f.close()


process_file()
