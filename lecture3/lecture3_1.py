# this code example demonstrates the problems of float data type with certain values
from decimal import Decimal
import math

# this is a somewhat tedious feature of the float data type
number1 = float(0.1)
number2 = float(0.2)
print(f"Normal float/decimal numbers: {number1} + {number2} =")
print(number1 + number2)

# easy / common way, just round the value:
total = number1 + number2
total = round(total, 1)
print(total)

# option 2: you can use the Decimal-module
number3 = Decimal("0.1")
number4 = Decimal("0.2")
print(f"Decimal numbers of the Decimal-module: {number3} + {number4} =")
print(number3 + number4)