from functions import *

# we can simplify code by placing
# the repeating structure into a function
numbers = [1, 5, 3, 6, 2, 8, 9]
grades = [5, 4, 5, 2, 3, 4, 1]
temperatures = [-18, -14, -8, -11, -32, -15, -17]

# notice how the logic repeats itself
# even if the variables are different
average = get_list_average(numbers)
print(f"avg, numbers: {average}")

average = get_list_average(grades)
print(f"avg, grades: {average}")

average = get_list_average(temperatures)
print(f"avg, temperatures: {average}")
