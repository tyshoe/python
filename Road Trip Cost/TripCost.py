# 9. Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output
# their product and their average as integers (rounded), then as floating-point numbers.
# Output each rounded integer using the following:
# print(f'{:.0f}')
# Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
# print(f'{:.3f}')
# Ex: If the input is:
#
# 8.3 10.4 5.0 4.8
#
# the output is:
#
# 2072 7
#
# 2071.680 7.125

# this gets user input
num1_in, num2_in, num3_in, num4_in = input("Enter 4 floating point numbers with spaces between: ").split()

# this converts input string to floated numbers
num1 = float(num1_in)
num2 = float(num2_in)
num3 = float(num3_in)
num4 = float(num4_in)

# function to product
product = (num1 * num2 * num3 * num4)

# function to average
average = (num1 + num2 + num3 + num4)/4

print()
print("Integer Product and Average:")
print("{:.0f}".format(product), "{:.0f}".format(average))
print()
print("Floating Product and Average:")
print("{:.3f}".format(product), "{:.3f}".format(average))
