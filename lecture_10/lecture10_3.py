from functions import *

# ask the number from user
value = input("Give a number:\n")
value = int(value)

# use our own function to determine if number
# is odd or even
result = get_even_number_text(value)
print(result)