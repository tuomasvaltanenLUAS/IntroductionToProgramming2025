# ask user a discount code
discount_code = input("Give your discount code:\n")

# we keep the current active discount code saved in a variable
current_code = "WINTER25"

# with text data we usually use only == or !=
# we can't use > or < with text really
# for example: if "banana" > "firetruck" => doesn't make any sense
if discount_code == current_code:
    print("Discount to price, -20%!")
else:
    print("Normal price.")