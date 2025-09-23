# ask user's age (integer)
age = input("How old are you?\n")
age = int(age)

# ask user the month number when they would like to visit your shop
month = input("Which month you'd like to visit the store?\n")
month = int(month)

# conditional statement -> is age under 20?
# if it is => run the print-code below
if age < 20:
    print("You are less than 20 years old.")
elif age < 30:
    print("You are less than 30 years old.")
elif age < 40:
    print("You are less than 40 years old.")
else:
    print("You age is something else.")

# since the month of the store has nothing to do
# with the user's age, have a separate if-statement!
if month == 7:
    print("We're closed on July.")
    print("Back open in August, welcome!")

print("Thank you for using the application!")