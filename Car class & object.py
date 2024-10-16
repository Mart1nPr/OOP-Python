# Car class & objects

class Car:
    def __init__(self, manufacture, model, year, for_sale):
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.for_sale = for_sale
    def drive(self):
        return(f"youdrive {self.manufacture} vehicle")
    def stop(self):
        return(f"you stop {self.model}")  
    def car_details(self):
        return("{} {} {} {}".format(self.manufacture, self.model, self.year, self.for_sale))      

FirstCar = Car(manufacture="BMW", model="325i E30", year=1983, for_sale=18000)
SecondCar = Car(manufacture="Toyota", model="jzx81", year=1977, for_sale=15000)
ThirdCar = Car(manufacture="Audi", model="RS2", year=1994, for_sale=60000)
FourthCar = Car(manufacture="BMW", model="318i E36", year=1993, for_sale=6700)

print(
    "First car: ", FirstCar.car_details(),
    "Second car: ", SecondCar.car_details(),
    "Third car: ",ThirdCar.car_details(),
    "Fourth car: ",FourthCar.car_details(),
    )
