# THIS EXAMPLE IS A VERY COMMON STRUCTURE NEEDED
# IN THE EXERCISES!

# also an example how to ask a value from user instead

# PHASE 1
# ask all needed variables from user (input)
# and convert them to numbers if needed
# YOU CAN ASK MULTIPLE VARIABLES FROM USER
number1 = input("Give a number: ")
number1 = int(number1)

# PHASE 2: do the needed calculations as needed
# by the exercise
number2 = 100
result = number1 + number2

# PHASE 3: print the result to user in a nice output
print(f"Total: {result}")