from myfunctions import *

# parameters
month_consumption = 220
month_fee = 2.99
price_kwh = 11.87
years = 5

# get costs for 5 years by using own function
total_cost = get_energy_costs(years, month_consumption, price_kwh, month_fee)

# print end result
print(f"Arvio kustannuksista {years}v ajalta: {total_cost}€")
