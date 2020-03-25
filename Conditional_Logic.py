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


#########################################################################

num = input('Enter a number :')
num=int(num)

if num%2==0:
    print('Number is even')
else:
    print('Number is odd')

indian=['samosa','daal','naan']
chinese=['egg role','pot sticker','fried rice']
italian = ['pizza','pasta','risotto']

dish=(input('Enter dish name: ')).lower()



if dish in indian:
    print('Indian cuisine')
elif dish in chinese:
    print('Chinese cuisine')
elif dish in italian:
    print('Italian Cuisine')
else:
    print('Based on little knowledge I have, I dont know which cuisine is ',dish)


######################################
usa=['atlanta','new york','chicago','baltimore']
uk = ['london','bristol','cambridge']
india=['mumbai','delhi','banglore']

## Write a program that asks user to enter a city name and it should tell you which country it belongs to

city =(input('Enter city name : ')).lower()

if city in usa:
    print('You are from USA')
elif city in uk:
    print('You are from UK')
elif city in india:
    print('You are from India')
else:
    print('Your country not known to me')

##Write a program that asks user to enter two cities and tell you if they both are in same country or not

city1 =(input('Enter your first city :')).lower()
city2 = (input('Enter your second city :')).lower()

if city1 in usa and city2 in usa:
    print('Both cities belong to USA')
elif city1 in uk and city2 in uk:
    print('Both cities belong to UK')
elif city1 in india and city2 in india:
    print('Both cities belong to India')
else:
    print('Entered cities belong to different countries')

