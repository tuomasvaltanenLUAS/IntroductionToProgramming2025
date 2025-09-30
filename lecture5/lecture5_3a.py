# ask user for some text
text = input("Write a sentence:\n")

# calculate amount of characters in the user's text
# NOTE: empty spaces are also characters
text_length = len(text)

# print result
print(f"Text length: {text_length} characters!")

# text_length is just like any integer, use it as you wish
if text_length > 30:
    print("LONG TEXT!")

    # text is too long, shorten it to fit the screen better
    shortened = text[0:30] + "..."
    print(shortened)
else:
    print("Short text...")

# a common if-statement would be to test if user's password
# is at least 15 characters long etc.

# count the amount of letters, this case lowercase 'a'
# NOTE: uppercase and lowercase letters ARE COMPLETELY
# different letters in programming, because otherwise
# the code would never know when to print an uppercase
# or lowercase letter onto the screen
a_letters = text.count("a")
print(f"Amount of a-characters: {a_letters}")