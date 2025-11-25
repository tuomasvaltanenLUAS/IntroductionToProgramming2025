def factorial(number):
    if number == 1:
        return number
    else:
        next_number = number - 1
        total = number * factorial(next_number)
        return total


print()
print(factorial(5))
print()