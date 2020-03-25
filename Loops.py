#Loop through a collection

people = ['Christopher' , 'Susan']
for name in people:
    print(name)


#Looping a number of times

for index in range(0, 2):
    print(index)


#Looping with a condition

names = ['Christopher' , 'Susan']
index = 0
while index < len(names):
    print(names[index])
    #Change the condition!!
    index= index + 1


####################################################################################

exp=[2340,2500,2100,3100,2980,]

# total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
total =0
for item in exp:
    total = total + item
print(total)

for i in range(1,11):
    print(i)

## Monthwise expense and total expense
total = 0
for i in range (len(exp)):
    print('Month:',(i+1),'Expense:',exp[i])
    total = total + exp[i]

print('Total expense is: ',total)

## Find the key from differnt location in list

key_location='chair'
locations=['garage','living room','chair','closet']

for i in locations:
    if i==key_location:
        print('Key is found in',i)
        break
    else:
        print('Key is not found in', i)


## Print square of numbers between 1 to 5 EXCEPT even numbers

for i in range (1,6):
    if i%2==0:
        continue
    print(i*i)


i=1
while i<=5:
    print(i)
    i=i+1


## After flipping a coin 10 times got this result,
## result = ['heads','tails','tails','heads','tails','heads','heads','tails','tails','tails']
##Using for loop figure out count for 'heads'.

result = ['heads','tails','tails','heads','tails','heads','heads','tails','tails','tails']
count_heads=0
for i in result:
    if i=='tails':
        continue
    # print(i)
    count_heads=count_heads+1
print('Number of times heads came are: ',count_heads)

## Another way
c=0
for i in result:
    if i=='heads':
        c=c+1
    else:
        continue
print(c)


## Your monthly expense list (from Jan to May) looks like this,
## expense_list = [2340,2500,2100,3100,2980]
## Write a program that asks you enter an expense amount and program should tell you the month in which that 
##expense occured. If the expense is not found then convey that as well.

expense_list = [2340,2500,2100,3100,2980]

expense_amt = int(input('Enter the Expense amount: '))
m=0
for i in expense_list:
    if i == expense_amt:
        m=m+1
        print('Month :',m, 'Expense :', expense_amt)
        break
    else:
        m=m+1
        print('not availble in Month: ',m)



## Write a program that prints following shape,(Hint: Use for loop inside another for loop)
##  * ** *** **** *****
num=int(input('Enter number of rows: '))
for i in range(1,num):
    for j in range (1,i+1):
        print('*',end=' ')
    print()
