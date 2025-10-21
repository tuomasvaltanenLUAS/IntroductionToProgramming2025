# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer", "Fridge",
            "Toothbrush", "Microwave", "Bookshelf", "Oven",
            "Snowblower", "Mouse", "Table"]

# let's build a text variable in a loop
text = ""

# loop through your products
# you could use .join() -function too (we learn this later)
for single_product in products:
    text = text + single_product + ", "

# print the text variable after loop
print(text)

