from datetime import date, datetime, timedelta

# two timestamps
first = date(2025, 9, 15)
second = date(2025, 12, 31)

# calculate the difference
delta = second - first
days = delta.days

# print the result
print(f"Days left this year: {days}")

# example 2, if we create a bill for a customer today
# what is the due date in 3 weeks (21 days), also could be used
# for warranties etc.
today = datetime.now()
today = today + timedelta(21)

# format nicely and print
date_text = today.strftime("%d.%m.%Y")
print(date_text)