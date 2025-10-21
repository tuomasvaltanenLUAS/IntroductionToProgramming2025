# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer",
            "Fridge", "Toothbrush", "Microwave"]

# ask the index from the user
choice = input("Which product would you like to modify?\n")
choice = int(choice)

# ask the name of the new replacement product
new_product = input("What is the name of the replacement product?\n")

# replace the product with given index and name
# add needed if/else or try/except if user tries
# to modify a non-existing index
products[choice] = new_product

# let's quickly check if this worked
print(products)