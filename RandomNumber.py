import random

#print(dir(random))

value = random.random()
print(value)

value1 = random.uniform(1,10)
print(value1)

value2 = random.randint(0,10)
print(value2)

##Function to generate random number as string

def randomNumber(numberLength):
    number = ('0','1','2','3','4','5','6','7','8','9')
    return ''.join(random.choice(number) for i in range (numberLength))

print ('Random number is : ', randomNumber(10))