# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer",
            "Fridge", "Toothbrush", "Microwave"]

# always get the amount of elements in the list BEFORE THE LOOP
# because most programming languages will otherwise
# re-calculate the amount of elements on EACH CYCLE, which is not needed
amount = len(products)

# if you have 6 products
# this would be the same as for x in range(6) etc.
# don't use len() directly in the range() for the loop
# (e.g. for index in range(len(products)):
# because this way the loop calculates the amount of data
# again after each cycle
# so if you have 10000 products => 10000 unnecessary calculations
for index in range(amount):
    p = products[index]
    print(f"{index + 1}: {p}")