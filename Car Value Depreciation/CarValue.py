# sample run
# Please input the year of your car: 2018
# Please input the purchase price of you car: 32000
# Please input the current year: 2018
# Car's information:
# Model year: 2018
# Purchase price: 32000
# Current Value: 32000

class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        print("Car's information:")
        print("Model year:", self.model_year)
        print("Purchase price:", self.purchase_price)
        print("Current Value:", self.current_value)


year = int(input("Please input the year of your car: "))
price = int(input("Please input the purchase price of you car: "))
current_year = int(input("Please input the current year: "))

my_car = Car()
my_car.model_year = year
my_car.purchase_price = price
my_car.calc_current_value(current_year)
my_car.print_info()
