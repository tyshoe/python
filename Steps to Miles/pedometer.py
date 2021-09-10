# Problem 2
# A pedometer treats walking 2,000 steps as walking 1 mile.
# Write a program whose input is the number of steps, and whose output is the miles walked.
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f}'.format(your_value))

user_steps = float(input("Enter steps: "))
miles = float(user_steps)

# changes steps to miles


def steps_to_miles(user_steps):
    miles = user_steps / 2000
    float(miles)
    print("You walked:", '{:.2f}'.format(miles), "miles")
steps_to_miles(user_steps)

