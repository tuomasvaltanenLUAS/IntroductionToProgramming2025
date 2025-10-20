# use loops to automate parts of code
total = 0

# use loop to ask 10 numbers from user
# and add it total
# basically we automate a repeating input-structure
# in our code this way!
for x in range(10):
    number = int(input("Give a number:\n"))
    total = total + number

print("Total sum of the numbers:")
print(total)