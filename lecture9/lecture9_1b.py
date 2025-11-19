# another version of list of lists

# product categories in a webstore
books = ["Lord of the Rings", "Da Vinci Code", "Robinson Crusoe"]
movies = ["Interstellar", "Forrest Gump", "Jurassic Park"]

# list of lists => all product categories in one => all products
products = [books, movies]

# TRY THIS IN PYTHON TUTOR

# since products is a LIST OF LISTS
# we need a FOR loop with another FOR loop
for category in products:
    # for each product item in current active category
    for item in category:
        print(item)