# ask user for some input
text = input("Give a value:\n")

# you can use this as the basis of exercise 4-7
# e.g. 12345 => number, "one two three four five" -> text

# additional idea, if you want to also use isnumeric()
# with decimal values, try removing the decimal separator
# e.g. text_new = text.replace(".", "")

if text.isnumeric():
    print("User gave numbers...")

    # IN THIS PHASE, we can be certain, text contains a number
    # which means we can convert this to int/float
    number = int(text)
    result = number * 2
    print(f"Number doubled: {result}")
else:
    print("User gave text!")