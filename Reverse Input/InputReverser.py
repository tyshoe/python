# Problem 4
# Write a program whose input is two integers and whose output is the two integers swapped.
# Your program must define and call the following function. swap_values() returns the two values in swapped order.
# def swap_values(user_val1, user_val2)
user_val1, user_val2 = (input("Enter two integers separated with a space: ").split())


def swap_values(user_val1, user_val2):
    x = user_val1
    user_val1 = user_val2
    user_val2 = x
    print(user_val1, user_val2)


swap_values(user_val1, user_val2)
