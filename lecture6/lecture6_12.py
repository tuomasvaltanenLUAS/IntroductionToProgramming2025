# allow the user to choose the amount
# of cycles in the for loop later
cycles = input("How many numbers to ask?\n")
cycles = int(cycles)

# initialize the sum variable
total = 0

# using cycles from user to determine the amount
# of cycles in the for loop
for x in range(cycles):
    number = int(input("Give a number:\n"))
    total = total + number

print("Total sum of the numbers:")
print(total)