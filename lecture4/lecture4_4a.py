# TASK 1: Create an application that greets the users
# based on given hour of the current time. Convert the given hour into
# integer format. Use the following logic while greeting the user:

# If hour is 05 - 11: respond "Good morning"
# If hour is 12 - 17: respond "Good afternoon"
# If hour is 18 - 21: respond "Good evening"
# If hour is 22 - 04: respond "Good night"

# PHASE 1: ask the needed variable from user
hour = input("Give the current hour:\n")
hour = int(hour)

# PHASE 2: program logic -> greet the user based on instructions above
if 5 <= hour <= 11:
    print("Good morning!")
elif 12 <= hour <= 17:
    print("Good afternoon!")
elif 18 <= hour <= 21:
    print("Good evening!")
else:
    print("Good night!")







# EXTRA TASK (we'll do this last):
# if the user doesn't provide the hour (empty input)
# get the current hour from datetime-module