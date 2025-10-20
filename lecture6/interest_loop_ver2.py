# compound interest calculator, LOOP VERSION
# VERSION 2: how many years does it take to accumulate
# a certain amount of profit
start_money = 25000
interest = 1.085

# let's allow the user to add more money every year
yearly_money = 2000

# define the total-variable
total = start_money
current_profit = 0
target_profit = 125000

# use Python to calculate interest 10 years in a row
for year in range(1, 31):
    total = total + yearly_money
    total = total * interest

    # calculate how much profit we currently have for the if-statement below
    current_profit = total - start_money - (year * yearly_money)

    # check if we have exceeded our target
    # if yes => break => end the loop (no point looking further
    # because we found our answer)
    if current_profit >= target_profit:
        print(f"We met our goal in the year: {year}")
        break


if current_profit < target_profit:
    print("This goal cannot be achieved within this time frame and investments.")

