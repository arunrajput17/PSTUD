## Always prefix test_ for the files having unit test methods

import mathlib_1    

## Always give test_ prefix to all the functions

def test_calc_total():
    total = mathlib_1.calc_total(4,5)
    assert total == 9

def test_calc_multiply():
    result = mathlib_1.calc_multiply(10,3)
    assert result == 30

def  test_calc_subtract():
    sub_result = mathlib_1.calc_subtract(20,5)
    assert sub_result == 15

####################################
## Ways of executing

# python -m pytest
# First it will look under all the files and directory and look for any file which have test_ prefix
#and in that file it is going to execute all the test which has test_ prefix in front of method
# 

# py.test
# When you say this it will run all the test

# py.test -v
#If you want to see detail output there is -v command which means verbose . When you do that it will
# list down the test name and whether it is passed or fail


