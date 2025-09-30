# you could also ask this from user
text = input("Write some text:\n")

# from first character 10th
# REMEMBER: empty space is also a character
# these examples are also very helpful in the
# exercise set 4-3
subtext1 = text[0:10]
print(subtext1)

# take a partial text from the middle
# start at position 10 (starting from 11th), until 15th character
subtext2 = text[10:15]
print(subtext2)

# take all characters after 6th character
subtext3 = text[5:]
print(subtext3)

# get last five characters by using negative index
# basically, start from the 5th character FROM THE END,
# and take all that is towards left
subtext4 = text[-5:]
print(subtext4)

# EXTRA: sometimes handy, just remove the final character
# often some kind of extra mess we have to clean up
subtext5 = text[0:-1]
print(subtext5)