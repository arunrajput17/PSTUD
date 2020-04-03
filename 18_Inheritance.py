## Inheritance

## Benefits of Inheritance
# 1. Code reuse
# 2. Extensibility
# 3. Readability


class Vehicle:      # Parent Class
    def general_usage(self):
        print('general use: transportation')


class Car(Vehicle): #First Child class
    def __init__(self):
        print('I am car')
        self.wheels = 4
        self.roof = True

    def specific_usage(self):
        print('specific use: commute to work, vacation with family')


class MotorCycle(Vehicle):  # Second child class
    def __init__(self):
        print('I am motor cycle')
        self.wheels =2
        self.roof= False

    def specific_usage(self):
        self.general_usage()    # Calling parent class function
        print('specific use: road trip, racing')

c = Car()
c.general_usage()   # Calling Parent class function from child one class object
c.specific_usage()

m = MotorCycle()
m.specific_usage()



## isinstance and issubclass methods

ca = Car()
mo = MotorCycle()

# isinstance: it will tell if an object is an instance of specific class or not
print(isinstance(ca,Car))
print(isinstance(ca,MotorCycle))

# issubclass: It will tell if one class is sub class of another or not
print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))
