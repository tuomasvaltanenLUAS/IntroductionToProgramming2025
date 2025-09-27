# TASK 3: Create an application that asks the user the name of the product
# and the amount of products they wish to buy.
# for example: they want to buy 10 smartphones etc.

# Also ask if the user has a discount voucher (yes/no)

# the pricing is the following:
# - smartphone = 599 € per item
# - computer = 899 € per item
# - coffee machine = 129 € per item

# calculate the total price of the user's products

# if the user has a discount voucher, reduce 15% from the total price

# Finally, print the price rounded to two decimals and inform
# the user IF a voucher was used to reduce the price.
# If no voucher used, don't mention it.

# things to think about:
# do we need nesting?
# do we need if-elif or separate if -structures
# ...or do we need both?

# EXAMPLE SOLUTION:

# PHASE 1: Ask needed variables from user
product = input("Which product you wish to buy? (smartphone, computer, coffee machine)\n")
amount = input("How many items of this product would you like to buy?\n")
amount = int(amount)

# voucher, yes/no
discount = input("Do you have a discount voucher? (yes/no)\n")

# initialize result variable
total = 0

# having two separate structures of if
# if-elif-etc for price logic and if-else for voucher
# is probably the most straight-forward approach here

# PHASE 2: price logic
if product == "smartphone":
    total = amount * 599
elif product == "computer":
    total = amount * 899
elif product == "coffee machine":
    total = amount * 129
else:
    print("Unidentified product.")

# voucher logic
if discount == "yes":
    # 15% discount => 1 - 0.15 => 0.85
    total = total * 0.85

# PHASE 3: round values and print
total = round(total, 2)
print(f"Total price: {total} €")