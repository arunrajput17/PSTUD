## Sometimes you can combine condition with AND instead of nesting if statements.

# A student makes honor roll if their average is >=85
# and their lowest grade is not below 75

gpa = float(input('What was your Grade Point Average? '))
lowest_grade= float(input('What was your lowest grade? '))

if gpa >= .85:
    if lowest_grade >= .70:
        print ('You made the honor roll')


if gpa >= .85 and lowest_grade >= .70:
    print ('You made the honor roll 2')


# If you need to remember the results of a condition check later in your code,
# use the Boolean variables as flags

if gpa >= .85 and lowest_grade >= .70:
    honor_roll = True
else:
    honor_roll = False
#if somewhere later in your code
if honor_roll:
    print('You made the honor roll 3')

