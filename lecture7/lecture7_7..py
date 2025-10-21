products = ["ORDER123_A7785_2025", "ORDER234353_C13856_2024",
            "ORDER2fadsfsda34353_Cfasdafsd3856_2023"]

# don't use substring for splitting a string liek this
# use split() -instead, since now it doesn't matter
# what length each part has, it always works!
for product in products:
    parts = product.split("_")

    order = parts[0]
    code = parts[1]
    year = parts[2]

    print(order)
    print(code)
    print(year)
    print()

