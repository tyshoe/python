# 3. The following equations estimate the calories burned when exercising
# Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184
# Men: Calories = ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184
#
# Write a program using inputs age (years), weight (pounds), heart rate (beats per minute)
# and time (minutes), respectively. Output calories burned for women and men.
# Output each floating-point value with two digits after the decimal point.
#
# Ex: If the input is:
# 49 155 148 60
#
# Then the output is:
# Women: 580.94 calories
# Men: 891.47 calories

# gets user inputs but assigns them to str(variable)
age_in = input("Enter age in years : ")
weight_in = input("Enter weight in pounds : ")
heart_rate_in = input("Enter heart rate in beats per minute : ")
time_in = input("Enter time in minutes : ")

# reassigns user inputs to floats
age = float(age_in)
weight = float(weight_in)
heart_rate = float(heart_rate_in)
time = float(time_in)

# functions to calculate calories by gender
women_cal = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184
men_cal = ((age * 0.2017) + (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184
float(women_cal)
float(men_cal)
print("Women:", "{:.2f}".format(women_cal), "calories")
print("Men:", "{:.2f}".format(men_cal), "calories")
