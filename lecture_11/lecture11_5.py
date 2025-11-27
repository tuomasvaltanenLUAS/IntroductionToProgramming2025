# open our text file (create connection) in APPEND mode
# creates the file if it's missing (mynotes.txt)
# we'll use UTF-8 as character encoding
# in order to avoid garbled mess with Finnish Ä or Ö etc.
file_handle = open("mynotes.txt", "a", encoding="utf-8")

# ask text from user
message = input("Write your message:\n")

# write the data into the file
# add new line \n in order to place all
# messages into separate lines in the file
file_handle.write(message + "\n")

# let's close the file connection (good practice)
file_handle.close()

print("Thank you for using our service.")