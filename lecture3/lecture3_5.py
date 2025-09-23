# ask one number from user => convert to int()
# especially with conditionals, because we might
# compare numbers to text
number1 = input("Give a number:\n")
number1 = int(number1)

# this could also be asked from user
number2 = 234

# if one of these variables is still in text format
# (no int/float used), this can be very buggy
if number1 > number2:
    print("The user's number is bigger!")
else:
    print("The other number is bigger...")