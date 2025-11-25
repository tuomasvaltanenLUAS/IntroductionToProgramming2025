from functions import *

# reverse the text from the user
# with our helper functio
text = input("Give a text:\n")

# use our helper function to define
# if this text is a palindrome
result = check_palindrome(text)

# check the boolean that our function returned
# inform the user of the result
if result:
    print("PALINDROME YES!")
else:
    print("NOT A PALINDROME!")