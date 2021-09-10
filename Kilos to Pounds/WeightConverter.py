# Problem 1
# Complete a program that takes a weight in kilograms as input, converts the weight to pounds,
# and then outputs the weight in pounds. 1 kilogram = 2.204 pounds (lbs).

kilos_in = input("Enter kilograms: ")
kilos = float(kilos_in)
# changes kilos to pounds


def kilo_to_pounds(kilos):
    pounds = kilos * 2.204
    float(pounds)
    print("Weight in pounds:", pounds, "lbs")


kilo_to_pounds(kilos)

