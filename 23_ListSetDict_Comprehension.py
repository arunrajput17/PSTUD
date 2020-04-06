## List / set / dict Comprehension : It provides a way to transform one list into another

# General way to find the even numbers from list is

numbers=[1,2,3,4,5,6,7,8,9]

even=[]

for i in numbers:
    if i%2 ==0:
        even.append(i)

print(even)

## Comprehension
even = [i for i in numbers if i%2==0]
print(even)

sqr_numbers =[i*i for i in numbers]
print (sqr_numbers)


## Set : set is an unordered collection of unique items.
# Set Comprehension

s=set([1,2,3,4,5,2,3])

print(s)

even ={ i for i in s if i%2==0}
print(even)


## Dict comprehension

cities =['mumbai','new york','paris']
countries =['india','usa','france']

#-- to create a dict where key is name of city and  value is country name

# zip is builtin function in python, it will zip two lists together

z = zip(cities,countries)
print(z)
for a in z:
    print(a)

# Comprehension

d ={city:countries for city, countries in zip(cities,countries)}
print(d)
