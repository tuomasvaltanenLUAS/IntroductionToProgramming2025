import json

# this is our data in our code, dictionary
phone = {
    "name": "Nokia 3310",
    "release_year": 2000,
    "battery": "1000mAh",
    "camera": False,
    "weight": 133
}

content = json.dumps(phone)

file_handle = open("myphone.json", "w")
file_handle.write(content)
file_handle.close()

print("Thank you adding your phone!")