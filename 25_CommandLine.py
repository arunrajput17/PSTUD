import argparse

### To reach till this folder in cmd follow this
# D:
# cd D:\Day Shift\Zpyth\Pstud

### Then run using
# python Practice.py
# python Practice.py -h

##### here we are writing a program that takes 3 inputs,
## 1. First number
## 2. Second number
## 3. Operation ('add','subtract','multiply')
## it should return result of operation based on inputs

# Two types of Arguments:

parser = argparse.ArgumentParser()


### 1. Positional

parser.add_argument('number1',help='first number')
parser.add_argument('number2',help='second number')

## if we dont want user to enter any other value then we can give him choices
# parser.add_argument('operation', help='operation')
parser.add_argument('operation', help='operation',\
    choices=['add','subtract','multiply'])




# 2. Optional

## To make argument optional just add -- in front of argument name then run as python Practice.py --number1 4 --number2 5 --operation add
# parser.add_argument('--number1',help='first number')
# parser.add_argument('--number2',help='second number')
# parser.add_argument('--operation', help='operation')


####################


args = parser.parse_args()

print(args.number1)
print(args.number2)
print(args.operation)

n1 = int(args.number1)
n2 = int(args.number2)
result = None

if args.operation =='add':
    result = n1 + n2
elif args.operation =='subtract':
    result = n1 - n2
elif args.operation =='multiply':
    result = n1 * n2
else:
    print('unsupported operation')

print ('Results:',result)
