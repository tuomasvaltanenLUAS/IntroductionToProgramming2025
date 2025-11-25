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


# define a function that calculates how many days
# are in given hours and returns the result
def hours_to_days(hours):
    result = hours // 24
    return result


# define a function that reverses a string
# this is a handy way to hide the weird
# Python way which reverses the string
def reverse_string(text):
    return text[::-1]


# define a function that checks if the given
# text is a palindrome or not
# (= text is identical also when reversed)
def check_palindrome(text):
    reversed_text = reverse_string(text)

    # check if the original text and reversed text match
    # return a Boolean
    if text == reversed_text:
        return True
    else:
        return False


# define a function that checks if the given
# order code follows the needed format, which is:
# exactly 10 characters longs, first letter is T
# this is a so-called validation function
def check_order(code):
    result = True

    # condition 1: length has to be exactly 10
    if len(code) != 10:
        result = False

    # condition 2: first letter has to be T
    if code[0] != "T":
        result = False

    return result
