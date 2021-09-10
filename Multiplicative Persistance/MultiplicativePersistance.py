# Write a program that takes in a positive parameter and returns its multiplicative persistence
# The additive persistence of 2718 is 2: first we find that 2 + 7 + 1 + 8 = 18,
# and then that 1 + 8 = 9. The multiplicative persistence of 39 is 3,
# because it takes three steps to reduce 39 to a single digit: 39 → 27 → 14 → 4.
# Also, 39 is the smallest number of multiplicative persistence 3.
user_input = int(input("Input a positive integer: "))
product = 1
pers = 0
while user_input > 9:
    for digit in range(0, len(str(user_input))):
        product *= int(str(user_input)[digit])
    pers += 1
    user_input = product
    product = 1
print("persistence:", pers)
