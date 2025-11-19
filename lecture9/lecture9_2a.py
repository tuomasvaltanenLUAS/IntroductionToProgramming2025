# dictionary inside another dictionary
book = {
    "name":  "My Lady Jane",
    "year":  2016,
    "publisher": {
        "name": "HarperTeen",
        "organization": "HarperCollins Publishers",
        "location": "New York"
    }
}

# printing the whole dictionary is usually a bit rough
# to understand what's going on, use indexes instead

# NOTE! we don't usually need loops with dictionaries
# Dictionaries are just collections of variables, and they are not
# super difficult to use
# but if you always TRY to use loops with dictionaries, then it's
# VERY difficult
# print(book)

print(book['name'])
print()

# how to use nested dictionaries, in this case publisher
# approach 1: save the nested dictionary into a helper variable
publisher = book['publisher']
print(publisher['organization'])

# approach 2: you can also chain these up directly
print(book['publisher']['organization'])