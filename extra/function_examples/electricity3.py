from myfunctions import *

# calculate costs for 5, 10 and 15 years
# otherwise same parameters
# params: years, month_consumption,  price_kwh, month_fee

total_cost_1 = get_energy_costs(5, 220, 11.87, 2.99)
total_cost_2 = get_energy_costs(10, 220, 11.87, 2.99)
total_cost_3 = get_energy_costs(15, 220, 11.87, 2.99)

# print results
print(f"Arvio kustannuksista 5v ajalta: {total_cost_1}€")
print(f"Arvio kustannuksista 10v ajalta: {total_cost_2}€")
print(f"Arvio kustannuksista 15v ajalta: {total_cost_3}€")
