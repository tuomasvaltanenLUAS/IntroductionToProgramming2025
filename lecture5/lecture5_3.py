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