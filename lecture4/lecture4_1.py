# our example variables, we could ask these from user too (input)
age = 22
city = "Helsinki"

# our code should give instructions to adult users
# based on their hometown and its health care services

# UNDERAGE USES should be directed to use their own school's
# health care services INSTEAD
if age >= 18:
    print("Adult instructions here!")

    # at this point we can be sure that the user is at least 18 years old
    # think these nested if-statements like a FOLLOW-UP question to the
    # previous if-statement
    if city == "Rovaniemi":
        print("Health care address for adults: Test Alley 12")
    elif city == "Helsinki":
        print("Health care address for adults: Somewhere Road 52")

else:
    print("Underage students: contact your school's health care services!")