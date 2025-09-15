# NEW FILE - another example of combining modules

# original half-life formula from here:
# https://mathsisfun.com/algebra/exponential-growth.html

import math
from datetime import datetime

# when we drank the last coffee
start_time = datetime(2025, 9, 15, 13, 0, 0)
end_time = datetime(2025, 9, 15, 21, 0, 0)

# how many hours ago?
duration = end_time - start_time
seconds = duration.total_seconds()
minutes = seconds / 60
hours = minutes // 60
hours = int(hours)

# let's assume half-life of coffee is 5 hours
half_life = 5

# let's assume our coffee cup is 300ml
cup = 300

# do the calculations
# half-life = cup * exp ^ (ln(0.5)/half_life)*hours
logarithm = math.log(0.5) / half_life
coffee_left = cup * math.exp(logarithm * hours)
coffee_left = int(coffee_left)

# print out the results
print(f"From the original {cup} ml of coffee I drank {hours} hours ago.")
print(f"{coffee_left} ml of coffee is still left in my body.")