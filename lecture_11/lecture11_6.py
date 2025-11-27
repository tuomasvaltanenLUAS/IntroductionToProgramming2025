import json

# open our text file (create connection) in READ mode
file_handle = open("app_data.json", "r")

# get raw JSON data (just text) from file
content = file_handle.read()

# content is just the raw JSON in string format
# JSON doesn't look like it, but it's actually text/string

# let's close the file connection (good practice)
file_handle.close()

# convert the raw JSON => Python data format
# after this you can use the city-variable
# as any other normal dictionary
city = json.loads(content)

print(city['name'])
print(city['population'])

# you can use this to compare
# how raw JSON and actual Python data
# are different
# import var_dump as vd
# print()
# vd.var_dump(content)
# print()
# vd.var_dump(city)
