# 8. Sites like Zillow get input about house prices from a database and provide nice summaries for readers.
# Write a program with two inputs, current price and last month's price (both integers).
# Then, output a summary listing the price, the change since last month
# and the estimated monthly mortgage computed as (current_price * 0.051) / 12.
#
# Output each floating-point value with two digits after the decimal point.
# Ex: If the input is:
#
# 200000 210000
#
# the output is:
#
# This house is $200000. The change is $-10000 since last month.
#
# The estimated monthly mortgage is $850.00.

# This makes it look better
print("House Prices")
print("Example input:")
print("If last month's price is [$200,000] and this month's price is [$210,000] enter(200000 210000)")
print()

# gets users inputs
lastPrice_in, currentPrice_in = input("Enter Last months price and then current price: ").split()

# redefines input string to integer value
lastPrice = int(lastPrice_in)
curPrice = int(currentPrice_in)

# monthly change function
change = (curPrice - lastPrice)

# mortgage functions
curPrice_Mortgage = ((curPrice * 0.051) / 12)

# pretty output and prints current price
print()
print("Current Price:", curPrice)

# if statement that determines if change is negative or positive or equal
if change < 0:
    change = change - (change * 2)
    print("This is", change, "cheaper than last month")
elif change == 0:
    print("There is no change in price from last month to this month")
else:
    print("This is", change, "more expensive than last month")

print("Estimated Monthly Mortgage: ", curPrice_Mortgage)
