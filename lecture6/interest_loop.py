# compound interest calculator, LOOP VERSION
start_money = 25000
interest = 1.085

# let's allow the user to add more money every year
yearly_money = 2000

# define the total-variable
total = start_money

# use Python to calculate interest 10 years in a row
for year in range(10):
    total = total + yearly_money
    total = total * interest

# calculate how much winnings we had
new_money = total - start_money - 10 * yearly_money
new_money = round(new_money, 2)

total = round(total, 2)

print(f"Total money: {total} €")
print(f"With given parameters, we earned this much money: {new_money} €")