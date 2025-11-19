# some random number data, what is the most common value here?
data = [3, 3, 3, 3, 3, 4, 5, 5, 3, 3, 5, 2, 3, 4, 1, 3, 5, 3, 4, 2]

# make a preliminary counting dictionary
result = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

# count each number in data and increase dictionary
# based on current value
for number in data:
    result[number] = result[number] + 1

# this is a bit "magic code line"
# but apparently it gets the highest value of a dictionary
# and prints out the result index
print(max(result, key=result.get))

# # if you want to generate these keys on the got
# # a more dynamic solution would be like this:
# for number in data:
#     if number not in result.keys():
#         result[number] = 0

# in this case: leave the result dictionary EMPTY in the beginning

print(result)