import random
import string

lower_upper_alphabet = string.ascii_letters
random_letter = random.choice(lower_upper_alphabet)
print(random_letter)

lower_alphabet = string.ascii_lowercase
random_lower_letter = random.choice(lower_alphabet)
print(random_lower_letter)

upper_alphabet = string.ascii_uppercase
random_upper_letter = random.choice(upper_alphabet)
print(random_upper_letter)

## Function to create random alphabet letters

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range (stringLength))

print(randomString(10))