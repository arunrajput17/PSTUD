## Functions can accept multiple parameters

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

print('Your initial is : ' + first_name_initial)
    
###################################################
## You can specify default value for a parameter
## like def get_initial(name, force_uppercase=True):
## call as get_initial(first_name)
###################################################

##You can also assign the values to parameters by name when you call the function
## i.e. get_initial(force_uppercase=True, name = first_name)

###################################################

## Using the named notation when calling the functions makes your code more readable

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('Oh no error: ' + error_message)
    #Imagine code here that logs our error to a database or file

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(45,1,True,'Second number greater than first', 'my_math_method')

### 
if first_number > second_number:
    error_logger(error_code=45,error_severity = 1,log_to_db=True,
    error_message='Second number greater than first', source_module='my_math_method')



