number = input("Give a number:\n")
number = int(number)

# if remainder of the number when dividin by 2
# is EXACTLY 0 => even number
# if not (else) => odd number
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")