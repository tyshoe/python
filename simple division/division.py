# 1. Write a program using integers user_num and x as input, and output user_num divided by x three times.
#
# Ex: If the input is:
#
# 2000 2
#
# Then the output is:
#
# 1000 500 250


# gets user number and converts string to float
str_user_num = input("Enter a number: ")
user_num = float(str_user_num)

str_x = input("Enter a number you want to divide the previous number by: ")
x = float(str_x)

print()
print("1st Division:", "{:.0f}".format(user_num/x))

# redefines user number
user_num = user_num/x
print("2nd Division:", "{:.0f}".format(user_num/x))

# redefines user number
user_num = user_num/x
print("3rd Division:", "{:.0f}".format(user_num/x))
