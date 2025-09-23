# THIS STYLE IS OFTEN USED IN WORKING LIFE
# basically we use conditional statements only
# TO OVERRIDE existing variables instead
# of trying to have all the code logic within if/else

# you can ask these from the user too
# input() =>  float() / int()
price = 200
age = 17

# if user is under 18 years old
if age < 18:
    # replace the original price with old price * 0.9 (10% discount)
    price = price * 0.9
else:
    # for customers 18 years old or more,
    # price is the old price + 4.95 € postage
    price = price + 4.95

# since we are modifying only the price in the if/else
# print out the price WHATEVER ITS VALUE IS RIGHT NOW
print(f"Total sum: {price} €")