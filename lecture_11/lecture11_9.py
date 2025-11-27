import json

# STEP 1: load the original JSON-file
# and convert it into Python -data format
# => list of dictionaries

# open our text file (create connection) in READ mode
# get raw JSON data (just text) from file
file_handle = open("american_cities.json", "r")
content = file_handle.read()
file_handle.close()

# convert the raw JSON => Python data format
# after this you can use the city-variable
# as any other normal dictionary
cities = json.loads(content)

for city in cities:
    print(f"{city['name']} ({city['state']})")
    print(f"Population: {city['population']}")
    print()

# STEP 2: ask details of a new city
# from the user (input) and create a new dictionary
# from scratch

# gather three variables from user
# population as integer
new_city_name = input("New city, name:\n")
new_city_population = int(input("New city, population:\n"))
new_city_state = input("New city, state:\n")

# construct the dictionary of the new city
new_city = {
    "name": new_city_name,
    "population": new_city_population,
    "state": new_city_state
}

# after we have a new dictionary => add the dictionary
# into the list of cities
cities.append(new_city)

# PART 3: save the new version of the cities list
# into the JSON file (override)
json_data = json.dumps(cities, indent=2)

# save the new version back into the file
file_handle = open("american_cities.json", "w")
file_handle.write(json_data)
file_handle.close()

print("Thank you for adding a new city.")