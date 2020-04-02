
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