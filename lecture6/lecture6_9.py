# more practical version of nested loops
print("Today's sales report:\n")

# our logic is this =>
# we have customer orders, each order has a certain amount of products

# so, orders => products
# we could also have even more complex stuff, like
# e.g. department => orders => products

# first, let's loop the orders (main loop)
for order in range(3):
    print(f"Start processing order no. {order + 1}")

    # process each product WITHIN this current order
    # here we assume each order has exactly 5 orders
    for product in range(5):
        print(f"\t\tProcessing order no. {order + 1}, product: {product + 1} ")

print("\nEnd of today's report (all orders processed).")