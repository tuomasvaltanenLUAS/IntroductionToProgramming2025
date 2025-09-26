# the logic of the weather is this

# Bad weather: if temperature is less than +10C
# Bad weather: if humidity is over 80%
# Bad weather: if wind speed is over 2.5 m/s
# Bad weather: if it's dark outside
# in this case, we can assume it's dark outside if time is
# between 20-24 or 0-7

# initialize variables
temperature = 5
humidity = 65
wind_speed = 1.5
hour = 10

# helper variables
sun_down = 20
sun_rises = 7

# initialize a Boolean, that only keeps track of the weather => is it good or bad
# we assume in the beginning the weather is good, and try to prove it worong
# with subsequent if-statements
good_weather = True

# let's try to formulate this condition somehow
# if you start to have a condition like this, CONSIDER A HELPER BOOLEAN VARIABLE
# to make logic easier and manageable

# this gets pretty complex quite easily... DOES THIS EVEN WORK?
# if temperature < 10 or humidity > 80 or wind_speed > 2.5 or (time > sun_down ...)

# temperature less than 10
if temperature < 10:
    good_weather = False

# if humidity is over 80%
if humidity > 80:
    good_weather = False

# wind_speed check
if wind_speed > 2.5:
    good_weather = False

# most difficult condition: time regarding dark
if hour > sun_down or hour < sun_rises:
    good_weather = False


# ALL CHECKS ARE DONE, we can now use our boolean to decide the outcome
if good_weather:
    print("Good weather outside!")
else:
    print("Bad weather... :(")