# this is a very good example, why collections are super powerful

# list of grades
grades = [2, 5, 1, 3, 4, 5, 2, 3, 1, 4, 5, 4, 3, 1, 3, 5, 5, 5]

# average = sum of values / amount of values
total = sum(grades)
amount = len(grades)

# calculate THE AVERAGE
average = total / amount
average = round(average, 1)
print(f"Average grade: {average}")