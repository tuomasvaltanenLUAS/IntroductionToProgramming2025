# start values
month_consumption = 220
month_fee = 2.99
price_kwh = 11.87
years = 5
year_consumption = month_consumption * 12
total_cost = 0

# calculate all years
for y in range(5):
    year_energy_cost = year_consumption * (price_kwh / 100)
    year_cost = (year_energy_cost + (12 * month_fee)) * 1.24
    total_cost += year_cost

    # prices increase each year
    price_kwh += 0.35
    month_fee += 0.15

# print end result
total_cost = round(total_cost, 2)
print(f"Arvio kustannuksista {years}v ajalta: {total_cost}€")
