# collections inside a collection
temp_day_1 = [13.5, 16.4, 11.6, 11.3]
temp_day_2 = [12.1, 15.2, 11.9, 10.4]
temp_day_3 = [15.3, 17.6, 12.5, 11.6]

# collections inside collections => list of lists
# e.g. this is the "main list" of the data
temperatures = [temp_day_1, temp_day_2, temp_day_3]

# raw printing format is mostly used (in working life)
# just to quickly check if there's any data at all
# for any other purpose, it's not usable
# (because nobody understands what's going on)
# print(temperatures)

# loop through each DAY in the main temperature list
for day in temperatures:
    print("NEW DAY STARTED!")

    # for the current active day
    # loop through each individual temperature MEASUREMENT
    # so we have x amount of days and a single day has y amount of temperatures
    for temp in day:
        print(temp)

    print()
