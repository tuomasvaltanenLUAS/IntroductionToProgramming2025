# do not create random.py -file anywhere in the project
# (just like with math-module), it will confuse the import
import random

# generate a random number
guess = random.randint(1, 10)
print(guess)

# let's generate two random dice, basic dice 1-6

# tip: you can duplicate a code file by selecting the file
# and pressing Ctrl + D (Windows)
# or CMD + D (Macintosh)
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print()
print(dice1)
print(dice2)

