# try this also in Python Tutor
# initialize an empty string variable
text = ""

# the idea is to build the text-variable
# from separate pieces within the loop
for year in range(2018, 2025):
    text = text + str(year) + "-"

# we can use substring to remove the final dash from the end
text = text[:-1]

# print the text-variable AFTER
# the loop has added all the years into it, one by one
print(text)