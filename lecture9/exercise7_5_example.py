import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# you need to find the weakest and strongest winds
# and their respective cities
strongest_wind = 0
strongest_wind_city = ""
weakest_wind = 0
weakest_wind_city = ""

# process each location in the data
for city in weather:
    print(city['location'])

    # get also the wind value
    wind = city['wind']
    print(wind)
    print()

    # place needed if-statements here to determine
    # strongest and weakest wind

    # NOTE! you can check for both weakest and strongest
    # winds in the same for-loop, NO NEED FOR TWO SEPARATE FOR-LOOPS!