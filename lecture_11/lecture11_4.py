# open our text file (create connection) in WRITE mode
file_handle = open("mynotes.txt", "w", encoding="utf-8")

# ask text from user
message = input("Write your message:\n")

# write the data into the file
file_handle.write(message)

# let's close the file connection (good practice)
file_handle.close()

print("Thank you for using our service.")