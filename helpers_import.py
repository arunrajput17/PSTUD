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


