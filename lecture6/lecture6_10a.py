print("Start!")

# for-loop that ends prematurely with break-command
for x in range(10):
    # if x is equal to 6 => stop the loop
    if x == 6:
        print("Data found, stop searching\n")

        # break stops the loop immediately
        # so if you wish to print something before that
        # do it before break (applies also to continue)
        break

    print(x)

print("End!")