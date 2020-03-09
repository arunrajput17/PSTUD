# If only one of the conditions will ever occur you can use a single if statement with elif

country = input('What country do you live in? ')
province = input('What province do you live in? ')
tax = 0

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavat':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15      #When you use elif instead of multiple if statements you can add a default action
print(tax)

# if multiple conditions cause the same action they can be combined into a single condition

if province == 'Alberta'\
    or province == 'Nunavat':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15 
print(tax)

# If you have list of possible values to check, you can use IN operator

if province in ('Alberta','Nunavat','Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15 
print(tax)

# If an action is depends on a combination of conditions you can nest if statement

if country.lower() == 'canada':
    if province in ('Alberta','Nunavat','Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15 
else:
    tax = 0.0
print('Tax rate is: ' + str(tax))
