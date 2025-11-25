from functions import *

# text = "X123456789"
text = input("Give an order code:\n")

# use our function to check if the code
# has the required features (validation function)
result = check_order(text)

# interpret the result based on the returned Boolean
if result:
    print("Code OK!")
else:
    print("Code not OK...")