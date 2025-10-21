# let's create a tuple for weekdays
# NOTE: normal parentheses in tuples
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")

# ask the index from the user
choice = input("Which weekday would you like to know?\n")

# adjust the index so it matches with the tuple better
choice = int(choice) - 1

# get the weekday and print it
# NOTE! always square brackets when accessing a collection
text = weekdays[choice]
print(text)