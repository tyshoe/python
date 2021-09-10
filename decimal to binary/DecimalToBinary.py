# Problem 3
# Write a program that takes in a positive integer as input,
# and outputs a string of 1's and 0's representing the integer in binary.
# For an integer x, the algorithm is:
    # As long as x is greater than 0
    #  Output x % 2 (remainder is either 0 or 1)
    #  x = x // 2
user_num = int(input("Enter a positive integer: "))
# changes decimal to binary


def Dec_to_Bin(user_num):
    string = ''
    while user_num > 0:
        x = user_num % 2
        string = string + str(x)
        user_num = user_num // 2

    print("You number in binary: ", string[::-1])


Dec_to_Bin(user_num)
