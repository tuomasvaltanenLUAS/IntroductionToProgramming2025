import datetime
import pandas as pd
import requests
from io import StringIO

# get amount of days left this year
today = datetime.date.today()
future = datetime.date(today.year, 12, 31)
days_left_year = (future - today).days

# internet page, where we get the GDP table data for this code
data_url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# since this website blocks script-level HTML download
# let's define a user-agent and use requests -module instead
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )
}

# perform webscrape with requests and
# convert data to expected StringIO -format for pandas
resp = requests.get(data_url, headers=headers)
raw_html = StringIO(resp.text)

# inputs from user, country and current expected GDP for comparisons later
country = input("Country:\n")
current_gdp = input("Current GDP for this year for this country:\n")
current_gdp = int(current_gdp)

# get data from website
data_table = pd.read_html(raw_html)[2]
data_table = data_table.iloc[1:, :]

# initialize variables to be changed by the following for-loop
gdp_2025, gdp_2024, gdp_2023 = 0, 0, 0

for index, row in data_table.iterrows():
    # if we didn't find our country in data,
    # skip this country and search further in the table
    if row.iloc[0] != country:
        continue

    # set variables in int-format
    gdp_2025 = int(row.iloc[1]) - current_gdp
    gdp_2024 = int(row.iloc[2]) - current_gdp
    gdp_2023 = int(row.iloc[3]) - current_gdp

    # we found the country we need, break out of loop
    break

print()
print("Difference to current GDP comparing to 2025")
print(gdp_2025)
print("Difference to current GDP comparing to 2024")
print(gdp_2024)
print("Difference to current GDP comparing to 2023")
print(gdp_2023)

# get highest and lowest gdp value for later use
all_gdps = [gdp_2025, gdp_2024, gdp_2023]
smallest_gdp = min(all_gdps)
largest_gdp = max(all_gdps)

months_left_this_year = days_left_year / 30
months_left_this_year = int(months_left_this_year)

if months_left_this_year == 0:
    months_left_this_year = 1

# print out the results comparing to lowest and highest GDP comparisons
print()
print("Required increase of GDP per month this year if target is to exceed lowest GDP comparison:")
print(f"{smallest_gdp / months_left_this_year}")

print("Required increase of GDP per month this year if target is to exceed highest GDP comparison:")
print(f"{largest_gdp / months_left_this_year}")

