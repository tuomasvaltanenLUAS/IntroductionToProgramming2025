# create a dictionary
# containing all information regarding this
# one person in one "variable"
person = {
    "name": "Test Person",
    "age": 33,
    "city": "Rovaniemi"
}

# only print the whole dictionary for testing purposes
# because otherwise you might print out sensitive information to the user
# passwords, session data, etc.
# print(person)

# we don't usually use loop with dictionaries
# because we need to have full control what is printed and what is not

# print the name of the person
print("Person's name:")
print(person['name'])

# print the age of the person
print("\nPerson's age:")
print(person['age'])