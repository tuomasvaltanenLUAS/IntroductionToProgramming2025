# try-block has the code that has the potential
# to crash in some situation. in this case, our code assumes
# user always gives a number, but what if they give text instead?
# except-block is launched, if the error actually happens
# print error message etc.

try:
    number = input("Give a number:\n")
    number = int(number)
    print(number)
except ValueError:
    print("You wrote text, only numbers supported. Run app again!")