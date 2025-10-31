# see installation instructions for external
# Python modules in Moodle
from colorama import Fore, Back, Style

# change the text color
print(Fore.MAGENTA + "Different text color!")
print("Same rules for colors still apply!")

# switch also the background color
# the text color remains the same, because we didn't
# change Foreground, only the background
print(Back.LIGHTBLACK_EX + "Change the background too!")

# reset all back to default
print(Style.RESET_ALL)
print("Back to normal text representation!")