# our test data
drinks = "water, milk, coffee, tea, water"

# replace water with soda
# if you want to replace only the first water
# drinks = drinks.replace("water", "soda", 1)
drinks = drinks.replace("water", "soda")

# ask user for their drink selection
choice = input("What would you like to drink?\n")

# check if user's text was in the original text
# in other words, is the user's word in the drinks-variable
if choice in drinks:
    print("Drink found!")
else:
    print("We don't have that, sorry!")

