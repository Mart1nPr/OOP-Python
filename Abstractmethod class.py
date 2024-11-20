# Abstract method class

# Electric car
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

print("Cars")
tesla = Tesla("Tesla", 2024, 70, 500)
toyota = Toyota("Toyota", 2024, 70, 500)
suzuki = Suzuki("Suzuki", 2024, 70, 500)

tesla.battery_status()
toyota.battery_status()
suzuki.battery_status()

# Smart phone
class Smart_phone(ABC):
    def __init__(self, Battery_Level):
        self.Battery_Level = Battery_Level
    @abstractmethod
    def Battery_Status(self):
        pass
class Iphone(Smart_phone):
    def __init__(self, Battery_Level, hours):
        super().__init__(Battery_Level)
        self.hours = hours
        self.usage = (self.Battery_Level/100)*self.hours
    def Battery_Status(self):
        print(f"Battery level {self.Battery_Level}% and used hours {self.usage}")
class Samsung(Smart_phone):
    def __init__(self, Battery_Level, hours):
        super().__init__(Battery_Level)
        self.hours = hours
        self.usage = (self.Battery_Level/100)*self.hours
    def Battery_Status(self):
        print(f"Battery level {self.Battery_Level}% and used hours {self.usage}")
class Xiomi(Smart_phone):
    def __init__(self, Battery_Level, hours):
        super().__init__(Battery_Level)
        self.hours = hours
        self.usage = (self.Battery_Level/100)*self.hours
    def Battery_Status(self):
        print(f"Battery level {self.Battery_Level}% and used hours {self.usage}")

print()
print("Phones")
iphone = Iphone(70, 100)
samsung = Samsung(70, 130)
xiomi = Xiomi(70,140)

iphone.Battery_Status()
samsung.Battery_Status()
xiomi.Battery_Status()
