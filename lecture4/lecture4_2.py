# application description: calculate train ticket price

# The logic is this:

# students get 50% discount always
# other users pay full price + 2.5 € service fee added
# if the ticket is over 100 €, no service fee

# ask user for the needed variables, convert price to decimal
status = input("Student or other? (s/o)\n")
price = input("Original ticket price? (€)\n")
price = float(price)

# make two different "lanes" for students and other students
if status == "s":
    # student-specific logic
    # students get -50% off the price
    price = price * 0.5
elif status == "o":
    # other customers -specific logic
    if price < 100:
        price = price + 2.5

# round the value to two decimals (since this is money)
price = round(price, 2)
print(f"Final ticket price: {price} €")