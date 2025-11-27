import json

# this is our data in our code, dictionary
phone = {
    "name": "Nokia 3310",
    "release_year": 2000,
    "battery": "1000mAh",
    "camera": False,
    "weight": 133
}

# we have to convert the complex Python data format into
# raw JSON format (which is basically just text (serialization))
# you can "prettify" the JSON data by using indent-parameter
# e.g. content = json.dumps(phone, indent=2)
content = json.dumps(phone)


# since content-variable is just text (JSON)
# we can just save it to a file
# always use w-mode with JSON data
# since a-mode will break the syntax of JSON
# making the data unusable
file_handle = open("myphone.json", "w")
file_handle.write(content)
file_handle.close()

print("Thank you adding your phone!")