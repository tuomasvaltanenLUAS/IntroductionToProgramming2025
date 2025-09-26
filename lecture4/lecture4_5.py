# TASK 2: Create a simple calculator, where user can perform
# one of the following operations: +, -, * and /

# in the beginning, ask the user for two numbers in float-format,
# ask finally which operation they would like to perform BETWEEN the numbers
# after the inputs, perform the selected operation between the numbers,
# if the selections were correct

# if user selects division (/), check that the second number is not 0.
# if user still gives a 0 as a second number, INFORM THE USER
# that we can't divide by zero

# if the user selects an operation that is not supported
# inform the user "Incorrect operation."

# print the result rounded to one decimal

# PHASE 1: ask the variables, convert as needed
number1 = input("Give first number:\n")
number1 = float(number1)

number2 = input("Give second number:\n")
number2 = float(number2)

operation = input("Which operation you would like to perform? (+, -, *, /)\n")

# create a variable before any conditionals, to keep track
# of final result
result = 0

# PHASE 2: program logic, decide which operation to perform
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    # check that we don't accidentally divide by zero
    if number2 == 0:
        print("Can't divide by zero!")
    else:
        result = number1 / number2

else:
    print("Incorrect operation")

# all calculations done, print the result
result = round(result, 1)
print(f"Result: {result}")