# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer", "Fridge"]

# ask the index from the user
choice = input("Which product would you like to see?\n")
choice = int(choice)

# as long as the index is an integer, we can also use a variable
# note: no conditional statements needed
# this is one of the reasons why professionals
# use collections all the time
text = products[choice]
print(text)