# 5. Given input characters for an arrowhead and arrow body, print a right-facing arrow.
#
# Ex: If the input is:
# *
# #
# Then the output is:
#               #
# * * * * * * * # #
# * * * * * * * # # #
# * * * * * * * # #
#               #

# gets user input
symbol1 = input("Enter first symbol: ")
symbol2 = input("Enter second symbol: ")

# formatting arrow
print(symbol1.rjust(7, ' '))
print(symbol1.rjust(7, symbol2).ljust(9, symbol1))
print(symbol1.rjust(7, symbol2).ljust(11, symbol1))
print(symbol1.rjust(7, symbol2).ljust(9, symbol1))
print(symbol1.rjust(7, ' '))
