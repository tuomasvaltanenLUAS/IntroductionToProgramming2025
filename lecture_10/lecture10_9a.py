# example of code, where we have LOTS OF REPETITION in the code
# which could be placed into a function

numbers = [1, 5, 3, 6, 2, 8, 9]
grades = [5, 4, 5, 2, 3, 4, 1]
temperatures = [-18, -14, -8, -11, -32, -15, -17]

# notice how the logic repeats itself
# even if the variables are different
total = sum(numbers)
amount = len(numbers)
average = total / amount
average = round(average, 2)
print(f"avg, numbers: {average}")

total = sum(grades)
amount = len(grades)
average = total / amount
average = round(average, 2)
print(f"avg, grades: {average}")

total = sum(temperatures)
amount = len(temperatures)
average = total / amount
average = round(average, 2)
print(f"avg, temperatures: {average}")