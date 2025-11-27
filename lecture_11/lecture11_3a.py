# open our text file (create connection) in READ mode
file_handle = open("weekdays.txt", "r")

# split the raw content of the file
# into a normal Python list of rows (lines)
content = file_handle.read()
lines = content.split("\n")

# let's close the file connection (good practice)
file_handle.close()

# just a normal list, loop through
# as you see fit
for line in lines:
    print(line)
