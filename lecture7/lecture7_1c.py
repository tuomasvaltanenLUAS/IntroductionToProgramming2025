# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer", "Fridge", "Toothbrush", "Microwave"]

# ask the index from the user
# NOTE: always use int() for index!
choice = input("Which product would you like to see?\n")
choice = int(choice)

# get the amount of products into a variable
# if you 4 products, this will be 4 etc.
# note how len() works for both texts and collections
amount = len(products)

# let's check if user gave a possible index
# in other words, 0-5 (if we have 6 products)
# you could also use try-except
# notice how resilient this code is for mistakes!
if choice >= 0 and choice < amount:
    # index OK, get the product
    text = products[choice]
    print(text)
else:
    print("No product given index.")

