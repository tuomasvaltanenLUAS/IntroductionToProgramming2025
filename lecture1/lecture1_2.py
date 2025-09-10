# traditionally you would have to convert
# numbers to text before combining them in to a bigger text
age = 25
age_text = str(age)

print("Your age is: " + age_text)

# luckily, we have a BETTER WAY today, f-string
number = 123

# see how the text and variables are combined within curly brackets
# kind of like replacing placeholders with variables
# f-string can also combine number and text automatically
print(f"Your number is: {number}, your age is: {age}")