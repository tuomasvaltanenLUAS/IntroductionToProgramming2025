# open our text file (create connection) in READ mode
file_handle = open("weekdays.txt", "r")

# split the raw content of the file
# into a normal Python list of rows (lines)
content = file_handle.read()
lines = content.split("\n")

# let's close the file connection (good practice)
file_handle.close()

# used in the loop below
amount = len(lines)

# just a normal list, loop through
# as you see fit
# e.g. for line in lines:
for index in range(amount):
    # get the line and print a numbered list
    line = lines[index]
    print(f"{index + 1} - {line}")
