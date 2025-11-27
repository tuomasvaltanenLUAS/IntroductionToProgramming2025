import json

# open our text file (create connection) in READ mode
file_handle = open("cities.json", "r")

# get raw JSON data (just text) from file
content = file_handle.read()

# convert the raw JSON => Python data format
# after this you can use the city-variable
# as any other normal dictionary
cities = json.loads(content)

for city in cities:
    print(f"{city['name']} ({city['capital']})")
    print(f"Population: {city['population']}")
    print()