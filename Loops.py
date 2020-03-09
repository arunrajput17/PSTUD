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