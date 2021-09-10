# Problem 5
# Write a program with total change amount as an integer input that
# outputs the change using the fewest coins, one coin type per line.
# The coin types are quarters, dimes, nickels, and pennies.
# Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.
# Your program must define and call the following function.
# The function exact_change() should return num_quarters, num_dimes, num_nickels, and num_pennies.
# def exact_change(user_total)
user_total = int(input("Enter a positive integer: "))


def exact_change(user_total):
    if user_total <= 0:
        print("You have no change")
    else:
        x = user_total
        print(x // 25, "quarters")
        x = x % 25
        print(x // 10, "dimes")
        x = x % 10
        print(x // 5, "nickels")
        x = x % 5
        print(x // 1, "pennies")
        x = x % 1


exact_change(user_total)
