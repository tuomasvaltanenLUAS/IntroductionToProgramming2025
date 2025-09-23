# ask user for product
drink = input("What would you like to drink?\n")

# if-elif-else -> structure
# -> react to different user responses
# else => drink not found

# kind of like a tree structure

if drink == "milk":
    print("Price of milk: 1 €")
elif drink == "coffee":
    print("Price of coffee: 8.5 €")
elif drink == "water":
    print("Free, drink from the tap.")
else:
    print("Drink not found.")