year = input("Give a year (2000 - 2012):\n")
year = int(year)

# easiest way to compare a bunch of range calues
# BUT!

# ALWAYS DOUBLE-CHECK ALL COMPARISONS
# AND TRY ALSO THE BOUNDARY VALUES

if 2000 < year <= 2004:
    print("2000-2004")
elif 2004 < year <= 2008:
    print("2004-2008")
elif 2008 < year <= 2012:
    print("2008-2012")
else:
    print("Incorrect year.")