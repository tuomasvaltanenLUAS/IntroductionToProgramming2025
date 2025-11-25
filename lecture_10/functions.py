# functions.py, this file contains
# the definitions of all our functions
# kinda like a toolkit, ready to be used
# by our other applications

# NOTE: a function does NOTHING in code
# unless it's used/called somewhere!

# define a function show_text()
# this means: "what should the code do, if something HAPPENED to
# call this function somewhere"
# this is like a blueprint for this function
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


# define a function that determines
# if a given number is odd or even
# and return the result as text
def get_even_number_text(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"