# 4. Given four values representing counts of quarters, dimes, nickels and pennies
# output the total amount as dollars and cents.
# Output each floating-point value with two digits after the decimal point.
#
# Ex: If the input is:
# 4 3 2 1
# where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels
# and 1 is the number of pennies, the output is:
# Amount: $1.41

# gets user inputs
quarters_in = input("Enter quarters : ")
dimes_in = input("Enter dimes : ")
nickels_in = input("Enter nickels : ")
pennies_in = input("Enter pennies : ")

# reassigns inputs to floats
quarters = float(quarters_in)
dimes = float(dimes_in)
nickels = float(nickels_in)
pennies = float(pennies_in)

# assigns quarter values
quarterValue = (quarters * .25)
dimesValue = (dimes * .10)
nickelsValue = (nickels * .05)
penniesValue = (pennies * .01)

# value equation
totalValue = (quarterValue + dimesValue + nickelsValue + penniesValue)
# print users dollar value
print("You have $", "{:.2f}".format(totalValue))
