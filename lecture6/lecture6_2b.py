# you sometimes need a range
# with year values
# e.g. 2018 - 2025

# with ranges, it's often a better idea
# to save the bounds into helper variables
start = 2018
end = 2025

# you can also define start and end of the range
# often used with year ranges, but otherwise
# surprisingly rarely used

# you can also use a third parameter
# that allows you to skip numbers in the for-loop
# in this case: print only every other number
for year in range(start, end, 2):
    print(year)