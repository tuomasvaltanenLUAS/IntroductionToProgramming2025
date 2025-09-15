import math

# use the math-module, and print the value of pi

# DON'T WRITE YOUR OWN PI VALUES IN A VARIABLE LIKE pi = 3.14
print(math.pi)
print()

# let's try a simple math equation
radius = 13

# circumference (border around the circle),
#     => 2 * pi      * radius
border = 2 * math.pi * radius

# remember to save the result of the rounding
# back to the variable (otherwise it doesn't work)
# e.g. just using round(border, 2) doesn't work!
border = round(border, 2)

print(f"Circumference: {border} cm")