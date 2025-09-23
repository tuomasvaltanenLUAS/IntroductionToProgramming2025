number = input("Give a number:\n")
number = int(number)

# is number between 0 and 30, or in other words
# is the number in the range of 0-30

# remember to READ OUT LOUD the whole conditional statement
# you often realize if it's wrong or not this way

# for example:
# IF number is bigger than 0 AND AT THE SAME TIME if number is less than 30
if number > 0 and number < 30:
    print("Number is in the range 0-30")

# IF number is less than 0 OR number is bigger than 30
if number < 0 or number > 30:
    print("Number is less than 0 or more than 30")
    print("Basically, this is the opposite of the previous statement.")