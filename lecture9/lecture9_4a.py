# example 1

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

# just printing the basic way, very hard to see the structure
# use a tool like var_dump instead
# print(hotels)
# vd.var_dump(hotels)

# sometimes easier to just inspect one dictionary
# first_hotel = hotels[0]
# vd.var_dump(first_hotel)

# you can copy the var_dump result as a code
# comment => easier to refer what the structure is!
# #0 dict(6)
#     ['name'] => str(16) "Snow Line Hotels"
#     ['rating'] => float(4.3)
#     ['wifi'] => bool(True)
#     ['free_breakfast'] => bool(True)
#     ['services'] => list(5)
#         [0] => str(5) "sauna"
#         [1] => str(8) "meetings"
#         [2] => str(10) "restaurant"
#         [3] => str(7) "parking"
#         [4] => str(7) "safaris"
#     ['price_level'] => int(4)

for hotel in hotels:
    print(hotel['name'])