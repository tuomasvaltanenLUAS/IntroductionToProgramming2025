# our list of dictionaries, products
products = [
    {"name": "Coffee maker", "price": 79},
    {"name": "Dishwasher", "price": 299},
    {"name": "Freezer", "price": 199},
    {"name": "Toothbrush", "price": 7},
]

# TRY THIS IN PYTHON TUTOR

# we have a list of dictionaries, so we need a loop
# each product (item) is one dictionary
# containing name and price
for item in products:
    name = item['name']
    price = item['price']

    # print the name and price of the active product
    print(f"{name} - {price} €")