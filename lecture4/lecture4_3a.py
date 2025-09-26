# example variables
# humidity => 0 - 100%
humidity = 88
temperature = -7

# initialize our helper control boolean variable: raining
# the ONLY PURPOSE of this variable is to KEEP TRACK of one question:
# IS IT RAINING OR NOT AT HTE MOMENT
raining = False

# in this part you would have all the possible logic
# that can alter that condition of the raining-variable
# THIS COULD BE 300-500 lines of code
if humidity > 80:
    raining = True

# another check, if temperature is subzero, it's no longer rain
if temperature < 0:
    raining = False

# YOU COULD HAVE HUNDREDS OR THOUSANDS OF LINES OF CODE HERE
# and even more if-statements that modify the Boolean

# with boolean logic, you usually have an if-statement
# like this IN THE END OF THE CODE, that handles the final
# situation of the boolean variable

# if raining ==> if raining == True
# if not raining ==> if raining == False
if raining:
    print("It rains!")
else:
    print("It doesn't rain.")