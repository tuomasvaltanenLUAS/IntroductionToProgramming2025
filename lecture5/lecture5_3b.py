# ask user for some text
text = input("Write a sentence:\n")

# calculate amount of characters in the user's text
# NOTE: empty spaces are also characters
text_length = len(text)

# check if given text is empty or not
# technically if text == "" often works too
if text_length == 0:
    print("Your text is empty!")
else:
    # not empty, print amount of characters
    print(f"Text length: {text_length} characters")