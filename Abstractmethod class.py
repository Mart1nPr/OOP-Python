# Abstract method class
from abc import ABC, abstractmethod
class Electric_Car:
    def __init__(self, brand_name, year, battery_level):
        self.brand_name = brand_name
        self.year = year
        self.battery_level = battery_level
    @abstractmethod
    def battery_status(self):
        pass
class Tesla(Electric_Car):
    def __init__(self, brand_name, year, battery_level, kilometers):
        super().__init__(brand_name, year, battery_level)
        self.kilometers = kilometers
        self.distance_passed = (self.battery_level/100)*self.kilometers
    def battery_status(self):
        print(f"Battery level {self.battery_level}% and distance passed {self.distance_passed}km")
class Toyota(Electric_Car):
    def __init__(self, brand_name, year, battery_level, kilometers):
        super().__init__(brand_name, year, battery_level)
        self.kilometers = kilometers
        self.distance_passed = (self.battery_level/100)*self.kilometers
    def battery_status(self):
        print(f"Battery level {self.battery_level}% and distance passed {self.distance_passed}km")
class Suzuki(Electric_Car):
    def __init__(self, brand_name, year, battery_level, kilometers):
        super().__init__(brand_name, year, battery_level)
        self.kilometers = kilometers
        self.distance_passed = (self.battery_level/100)*self.kilometers
    def battery_status(self):
        print(f"Battery level {self.battery_level}% and distance passed {self.distance_passed}km")


tesla = Tesla("Tesla", 2024, 70, 500)
tesla.battery_status()
        