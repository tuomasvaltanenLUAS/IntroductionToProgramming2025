# imports are file-specific, and you have to
# import everything again if you change the file

# coding style tip: always place ALL your imports
# on the top of for your file
# this way other programmers immediately see what is
# needed to install for this app
import math

# 3 to the power of 5, math-module way
number1 = math.pow(3, 5)
print(number1)

# Python also supports power itself
number2 = 3 ** 5
print(number2)

# don't do manual powering like this:
# side = 10
# total = side * side * side

# square root
number3 = 25
root_value = math.sqrt(number3)
print(root_value)

# for example, let's convert this formula
# into code, for example, the diagonal of a cube
# would be: d = sqrt(3) * a
side = 14

diagonal = math.sqrt(3) * side

print(f"The diagonal is {diagonal}")