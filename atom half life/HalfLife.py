# 7. A half-life is the amount of time it takes for a substance or entity to fall to half its original value.
# Caffeine has a half-life of about 6 hours in humans.
# Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, and 24 hours.
# Use a string formatting expression with conversion specifiers to output the caffeine amount as floating-point numbers.
# Output each floating-point value with two digits after the decimal point.
#
# Ex: If the input is:
# 100
# the output is:
# After 6 hours: 50.00 mg
# After 12 hours: 25.00 mg
# After 24 hours: 6.25 mg

# gets user input
mg_in = input("Enter the amount of caffeine in mg : ")
# redefines user input(string) to an floating point number
mg = float(mg_in)

# prints first half life
print("After 6 hours (1st Half Life) the amount of caffeine is :", "{:.2f}".format(mg/2), "mg")
# redefines mg so that calculation can be correct
mg = (mg/2)

# prints third half life
print("After 12 hours (2nd Half Life) the amount of caffeine is :", "{:.2f}".format(mg/2), "mg")
# redefines mg so that calculation can be correct
mg = (mg/2)

# prints fourth half life
print("After 24 hours (4th Half Life) the amount of caffeine is :", "{:.2f}".format(mg/4), "mg")
