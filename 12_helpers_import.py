## Importing a module

#import module as namespace
import helpers
helpers.display('Not a warning', True)

# import all into current namespace
from helpers import *
display('Not a warning 2')

# import specific item into current namespace
from helpers import display
display('Not a warning 3')

# To know how many functions in helpers module
print(dir(helpers))

###########################
## Modules is a way to reuse a code written by someone else

import math

print(math.sqrt(16))

print(math.pow(2,5 ))

## To know how many function are in MATH module Or you can google it
print(dir(math))

print(math.pi)
print(math.log10(100))

import calendar

cal= calendar.month(2020,1)
print(cal)
print(calendar.isleap(2020))
print(calendar.isleap(2019))

print(dir(calendar))


# How to import modules availble in different directory
import modules.mod_functions as f

area =f.calculate_square_area(5)
print(area)

### if this functions file is somwhere in the system then we need to import in this way

#  import sys
#  sys.path.append('C:\code')
#  import functions as f




