# " and ' do the same things => define a string (text variable)
# we can mix " and ' if we start with " and then '
# also vice versa
name = 'John "Supercoder" Doe'
print(name)

# for example, try using:
# name = "John "Supercoder" Doe"
# Python will be confused where text ends, and
# thinks Supercoder is a variable instead (breaks the syntax)

# also possible to flip the quotes
name = "John 'Supercoder' Doe"
print(name)

# we can also literally use quotation marks
# with the \-character => special character
name = "John \"Supercoder\" Doe"
print(name)

# by the end of the day, both of these are same
name2 = "John"
name3 = 'John'

print(name2)
print(name3)