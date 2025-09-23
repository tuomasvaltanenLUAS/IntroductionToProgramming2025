# ask the user if they are a student or not
choice = input("Are you a student? (y/n)\n")

# if is student
# notice how we have three different versions of this application
# based on the conditions!
if choice == "y":
    print("This code only runs when user is a student")
    print("For example, calculate a ticket price etc.")
elif choice == "n":
    print("Calculate price for other customer etc.")
else:
    print("Incorrect selection. Please restart the application.")