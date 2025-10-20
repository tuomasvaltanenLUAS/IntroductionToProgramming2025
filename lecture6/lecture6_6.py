print("START!")

# in while-loops, we have to take care of counter
# variable ourselves
counter = 1

# while-loop, in other words:
# RUN THIS CODE FOR AS LONG AS THE counter-variable
# is LESS OR EQUAL to 10
while counter <= 10:
    print(f"Cycle: {counter}")

    # you have to increase the counter yourself
    # or otherwise you get an infinite loop
    counter = counter + 1

print("END!")