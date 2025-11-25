# functions.py, this file contains
# the definitions of all our functions
# kinda like a toolkit, ready to be used
# by our other applications

# NOTE: a function does NOTHING in code
# unless it's used/called somewhere

# define a function show_text()
# this means: "what should my code do, if something HAPPENED to
# call this function somewhere"
def show_text():
    print("Welcome to our application!")
    print("---------------------------")
    print("Please follow the instructions.")
    print()


# another function: combine_text
# three parameters: first name, surname, age
# prints all information based on the parameters
def combine_text(first, last, age):
    print(f"Welcome: {first} {last}")
    print(f"You are {age} years old.")


# define a function that returns data
# => remember to save the result into a variable
def get_year():
    result = 2025
    return result
