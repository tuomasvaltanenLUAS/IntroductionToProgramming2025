# reversing a text in Python is quite different
# than in other languages, but hey, it works!
# basically this uses the substring-syntax
# but we choose all characters from beginning to end
# but TRAVERSE the string the other way (-1) (from end to beginning)
# [ : : -1]

text = input("Give text:\n")

# palindrome is a word that is the same forwards and backwards
# for example racecar
reversed_text = text[::-1]
print(reversed_text)