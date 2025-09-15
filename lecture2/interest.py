# compound interest, small demonstration how to combine all these modules

# compound interest (interest in interest) is a concept of return of investment
# where interest starts to accumulate interest on itself as well

from datetime import date
import math

# variables for the compound interest
start_money = 25000
interest_rate = 8.5

# calculate the amount of days between today and our target
# saving period time
start_date = date.today()
end_date = date(2035, 12, 31)

# how many years between the dates?
delta = end_date - start_date
days = delta.days
years = days // 365

print(f"Amount of years in this time span: {years}")

# compound interest, formula:
# final amount of money = start_money * (1 + interest_rate / 100) ^ years
total_money = start_money * math.pow(1 + interest_rate / 100, years)

# we still have the starting investment in the total money, let's remove it
new_money = total_money - start_money
new_money = round(new_money, 2)

print(f"With given parameters, we earned this much money: {new_money} €")