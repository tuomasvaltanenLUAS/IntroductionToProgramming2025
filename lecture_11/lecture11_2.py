# while-loop usually not the most practical
# solution due to having to fix the extra new lines
# from the original file etc.

# open our text file (create connection) in READ mode
file_handle = open("weekdays.txt", "r")

counter = 1

# infinite loop that keeps reading
# the file line by line until we
# arrive at the final row => we have to break out
# of the infinite loop
while True:
    # read one line at a time
    line = file_handle.readline()
    print(f"{counter}. {line}")

    # increase the line number counter
    counter = counter + 1

    # we reached the end of file => break out of loop
    if not line:
        break

# let's close the file connection (good practice)
file_handle.close()