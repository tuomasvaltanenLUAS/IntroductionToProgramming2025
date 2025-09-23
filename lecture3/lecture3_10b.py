number = input("Give a number:\n")
number = int(number)

# is number between 0 and 30
# this is the recommended SHORTHAND in Python
# for numeric range checks

# RECOMMENDED IN CERTAIN EXERCISES WHERE VALUE RANGES ARE PRESENT
if 0 <= number <= 30:
    print("Number is in the range 0-30 (including 0 and 30)")