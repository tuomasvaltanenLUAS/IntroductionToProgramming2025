# this is why it's a bit more sensible to use
# a specific import, if we use the normal import:
# import datetime
# we would have to use it like this:
# today = datetime.datetime.now()
from datetime import datetime

# get current time and data
today = datetime.now()
print(today)

# if we want to format the timestamp into a prettier format for the user
# we can use the strftime() -function

# the format we want: day.month.year hours:minutes:seconds
# %d = day, %m = month, %Y = year, %H = hour, %M = minute, %S = second

# if you want to remove the extra zeroes in days and months:
# in Windows: %#d and %#m
# in Unix / Linux / MacOS: %-d, %.m
date_text = today.strftime("%d.%m.%Y %H:%M:%S")
print(date_text)