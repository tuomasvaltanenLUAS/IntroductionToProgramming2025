# ANOTHER EXAMPLE, CLASSIC: FIBONACCI

# Fibonacci sequence: every number is the sum of two previous numbers
# first 9 numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21

# OUR GOAL: ask user a number: which Fibonacci number do they
# want to see, and count the value with a for-loop

# examples:
# if user inputs 5 = 1 + 2 = 3
# if user inputs 6 = 2 + 3 = 5
# if user inputs 7 = 3 + 5 = 8
# if user inputs 8 = 5 + 8 = 13
# x. number is old number + new number = fibonacci number

# helper variables to keep track of old and new number
old_number = 0
new_number = 1

# initialize fibonacci number to be 1 in the beginning
fibonacci = 1

choice = input("Which Fibonacci number would you like to see?\n")
choice = int(choice) - 2
print()

# for-loop that counts the Fibonacci number
# until the choice-variable dictates

for number in range(choice):
    print("New cycle!")
    # calculate the current value
    fibonacci = old_number + new_number

    print(f"Fibonacci is now: {old_number} + {new_number} = {fibonacci}")

    # update the old number
    old_number = new_number

    # update the new number to be whatever fibonacci is now
    new_number = fibonacci

    print(f"After this cycle: old_number = {old_number}, new number = {new_number}")
    print()

print()
print(f"Fibonacci number = {fibonacci}")