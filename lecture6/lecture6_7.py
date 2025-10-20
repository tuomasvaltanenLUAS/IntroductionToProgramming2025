# variable that controls if the app should be still running
running = True

# in this situation we can't know the exact amount
# of cycles, because we never know how many times the
# user wants to use this application
# this is why while-loop is more natural (compared to for-loop)
while running:
    print("Run app! Ask stuff from user, calculate something etc...")
    print()

    # here comes all the code that should be run on each cycle
    # => ask user inputs, calculate etc.
    number = input("Give a number:\n")
    number = int(number)

    # double the value and print it out
    total = number * 2
    print(f"Doubled: {total}")
    print()

    # ask user if they want to continue or exit app
    answer = input("Would you like to continue? (y/n)?\n")

    # check user's answer
    if answer.lower() == "n":
        running = False

# thank the user and end application
print("\nThank you for using the application! (END)")