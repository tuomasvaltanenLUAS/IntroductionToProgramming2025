from functions import *

# ask user for the amount of hours
# and convert to integer
hours = input("How many hours?\n")
hours = int(hours)

# use our helper function where
# we use the user's input as a parameter
days = hours_to_days(hours)
print(f"{days} in total.")