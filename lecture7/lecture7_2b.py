# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer", "Fridge",
            "Toothbrush", "Microwave", "Bookshelf", "Oven",
            "Snowblower", "Mouse", "Table"]

# let's build a text variable in a loop
text = ""

# loop through your products
# first cycle => first product
# last cycle => last product
for single_product in products:
    text = text + single_product + ", "

# print the text variable after loop
print(text)

