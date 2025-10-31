# see installation instructions for external
# Python modules in Moodle
from colorama import Fore, Back, Style

# ask user for a number
number = input("Give a number:\n")
number = int(number)

# check if user gave a positive number (or negative)
if number >= 0:
    print(Fore.BLACK + Back.LIGHTGREEN_EX + "Positive number!")
else:
    print(Fore.BLACK + Back.LIGHTRED_EX + "Negative number...")