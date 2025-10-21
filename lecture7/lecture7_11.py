# list of cities
cities = ["Rovaniemi", "Helsinki", "mikkeli", "Athens", "Madrid", "Stockholm"]

print("Original order:")
print(cities)

# sort the list, approach 1, modifies original order
# cities.sort()
# sorted_cities = sorted(cities)
#
# print("After sorting:")
# print(sorted_cities)
cities.sort(key=lambda v: v.upper())

print("After sorting:")
print(cities)