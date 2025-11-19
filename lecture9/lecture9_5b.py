import urllib.request
import json
import var_dump as vd

# get internet data
url = 'https://edu.frostbit.fi/api/events/en'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# convert the original raw JSON (text) format => Python data format
data = json.loads(raw_data)

# look at the data
# vd.var_dump(data)

# [0] => dict(4)
#     ['name'] => str(23) "HPO - Songs of the Ice "
#     ['date'] => str(10) "19.11.2025"
#     ['categories'] => list(3)
#         [0] => str(8) "concerts"
#         [1] => str(15) "cultural events"
#         [2] => str(5) "music"
#     ['address'] => dict(2)
#         ['street_address'] => str(19) "Mannerheimintie 13a"
#         ['postal_code'] => str(5) "00100"

# all set, loop through the events
for event in data:
    print(event['name'])