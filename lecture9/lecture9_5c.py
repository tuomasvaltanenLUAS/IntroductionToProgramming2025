# VERSION 2: simple search engine: filter only those event that
# matches user's choice
# e.g. ONLY SHOW THOSE EVENTS THAT MATCH THE CATEGORY OF USER'S INPUT

import urllib.request
import json
import var_dump as vd

# get internet data
url = 'https://edu.frostbit.fi/api/events/en'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# convert the original raw JSON (text) format => Python data format
data = json.loads(raw_data)

# user's search term for category
choice = input("What kind of events are you looking for?\n")

# all set, loop through the events
for event in data:
    # join the categories into a text and print
    categories = ", ".join(event['categories'])

    # if the user's choice is NOT in the categories => SKIP THIS EVENT
    # REMEMBER: continue => skip current iteration / cycle
    if choice not in categories:
        continue

    print(event['name'])

    # get the address info into separate variables
    street_address = event['address']['street_address']
    postal_code = event['address']['postal_code']

    # finally print the address info for the user
    print(f"{postal_code} {street_address}")

    # you should notice that one of events doesn't any categories
    # we have to catch that situation
    if len(event['categories']) > 0:
        print(f"CATEGORIES: {categories}")
    else:
        print("-- NO CATEGORIES --")

    print()