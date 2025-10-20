# you can also create a generic error handling
# but the error messages are often technical and straight from Python
# might also be a good idea to wrap a whole
# basic app around, so it doesn't crash in most cases
try:
    number = input("Give a number:\n")
    number = int(number)

    # note: this will crash, if user inputs 0 (can't divide by zero)
    result = 100 / number
    print(f"Result: {result}")

except Exception as e:
    print(f"Error message: {e}")
    print("Unknown error, please contact tech support.")
