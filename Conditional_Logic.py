# Your code needs the ability to take different actions based on different conditions

price = input('How much did you pay? ')
price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is :' + str(tax))



# You can add default action using else

if price >= 1.00:
    tax = .07
    print('Tax rate is :' + str(tax))
else:
    tax = 0
    print('Tax rate is :' + str(tax))

# How you indent your code changes execution

if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is :' + str(tax))


# Be carefull when comparing strings

country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')
