# example 1

# install via terminal:
# pip install var_dump
import var_dump as vd

# create first hotel
hotel_1 = {
    "name": "Snow Line Hotels",
    "rating": 4.3,
    "wifi": True,
    "free_breakfast": True,
    "services": ["sauna", "meetings", "restaurant", "parking", "safaris"],
    "price_level": 4
}

# create second hotel
hotel_2 = {
    "name": "North Ice Hostel",
    "rating": 3.5,
    "wifi": True,
    "free_breakfast": False,
    "services": ["sauna", "parking"],
    "price_level": 2
}

# place both hotels into one list
hotels = [hotel_1, hotel_2]

# create an empty list to catch all matching hotels later in the loop
restaurant_hotels = []

for hotel in hotels:
    print(hotel['name'])
    print("------------------------")

    # filter hotels that have a restaurant in our helper list
    if "restaurant" in hotel['services']:
        restaurant_hotels.append(hotel['name'])

    print()


# let's quickly see what was filtered
print(restaurant_hotels)

