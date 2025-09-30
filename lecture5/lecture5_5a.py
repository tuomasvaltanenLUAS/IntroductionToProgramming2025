# our test data
drinks = "water, milk, coffee, tea, water"

# replace water with soda
# if you want to replace only the first water
# drinks = drinks.replace("water", "soda", 1)
# you can also "remove" a word by replacing it with an empty string
# drinks = drinks.replace("water", "")
drinks = drinks.replace("water", "soda")
print(drinks)
print()

# you can replace any text with text, including new lines
new_drinks = drinks.replace(", ", "\n")
print(new_drinks)
