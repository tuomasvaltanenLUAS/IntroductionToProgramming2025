# RECAP: how to get data from users
# and how to use them in calculations

# THIS IS A TYPICAL STRUCTURE FOR MOST EXERCISES

# PHASE 1: get user input values

# ask the salary from user => convert to decimal (float)
salary = input("Give your salary:\n")
salary = float(salary)

# ask the savings too
savings = input("How much savings do you have?\n")
savings = float(savings)

# it's also fine to combine the float + input on the same line
# savings = float(input("How much savings do you have?\n"))

# PHASE 2: the actual calculation logic of the code
# this part usually starts to grow longer and more complex
# as we go further course

# we wish to increase the total +15%
increase = 1.15

# combine the input variables and apply the +15% increase
total = (salary + savings) * increase

# PHASE 3 - print out the result for the user
# USE F-STRING TO COMBINE TEXT AND NUMBERS EASILY
print(f"Total money: {total} €")