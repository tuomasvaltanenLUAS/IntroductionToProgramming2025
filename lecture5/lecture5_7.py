choice = input("Student or adult? (s/a)\n")

# before we attempt comparing the choice
# into "s" and "a" => convert choice to be
# always lowercase letter
# this way we can avoid complex comparisons
# like if text == "s" or text == "S" etc.
choice = choice.lower()

# check user's status, given by input
if choice == "s":
    print("You're a student!")
elif choice == "a":
    print("You're an adult!")
else:
    print("Incorrect selection.")
