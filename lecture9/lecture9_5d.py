# VERSION 3: simple search engine: filter only those event that
# matches user's choice
# e.g. ONLY SHOW THE FIRST EVENT THAT MATCHES THE QUERY
# forget the rest => find one / match one -logic
# break-command is useful here!

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
choice = input("What kind of an event are you looking for?\n")

# all set, loop through the events
for event in data:
    # join the categories into a text and print
    categories = ", ".join(event['categories'])

    # if the user's choice is in the categories
    # => we found a matching event
    # print the details and finally break out of the loop
    if choice in categories:
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
        break