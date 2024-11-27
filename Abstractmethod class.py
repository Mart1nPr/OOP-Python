# Abstract method class

# Electric car class
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

print("Cars class")
# Enter in order: Model, Year, Battery%, Hours until it reaches 0%
tesla = Tesla("Tesla", 2024, 70, 500)
toyota = Toyota("Toyota", 2024, 70, 500)
suzuki = Suzuki("Suzuki", 2024, 70, 500)

tesla.battery_status()
toyota.battery_status()
suzuki.battery_status()

# Smart phone class
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
print("Phones class")
# Enter in order: Battery%, Hours until it reaches 0%
iphone = Iphone(70, 100)
samsung = Samsung(70, 130)
xiomi = Xiomi(70,140)

iphone.Battery_Status()
samsung.Battery_Status()
xiomi.Battery_Status()


# Employee class
class Employee(ABC):
    def __init__(self, name, age, id_num, salary):
        self.name = name
        self.age = age
        self.id_num = id_num
        self.salery = salary
    @abstractmethod
    def calculate_pay(self):
        pass

class Full_time_Employee(Employee):
    def __init__(self, name, age, id_num, salary,hours,bonus):
        super().__init__(name, age, id_num, salary)
        self.hours = hours
        self.bonus = bonus
    def calculate_pay(self):
        if self.hours > 200:
            self.salery+=self.bonus
            print(f"{self.name} total salery is with bonus is: {self.salery}, hours {self.hours}")
        else:
            print(f"{self.name} total salery is with out bonus is: {self.salery}, hours {self.hours}")
class Part_time_Employee(Employee):
    def __init__(self, name, age, id_num, salary,hours,bonus):
        super().__init__(name, age, id_num, salary)
        self.hours = hours
        self.bonus = bonus
    def calculate_pay(self):
        if self.hours > 200:
            self.salery+=self.bonus
            print(f"{self.name} total salery is with bonus is: {self.salery}, hours {self.hours}")
        else:
            print(f"{self.name} total salery is with out bonus is: {self.salery}, hours {self.hours}")
class Intern(Employee):
    def __init__(self, name, age, id_num, salary,hours,bonus):
        super().__init__(name, age, id_num, salary)
        self.hours = hours
        self.bonus = bonus
    def calculate_pay(self):
        print(f"{self.name} salery is { self.salery}, Interns don't get bonuses. Hours {self.hours}")

# Enter in order: Name, Age, ID, Salery, Hours, Bonus
Tõnu = Full_time_Employee("Tõnu", 36, 5901204267, 2500, 240, 400)
Jurmo = Part_time_Employee("Jurmo", 30, 5940311269, 2500, 199, 400)
Jüri = Intern("Jüri", 18, 50612060269, 1050, 49, "No bonus")

print()
print("Employee class")
Tõnu.calculate_pay()
Jurmo.calculate_pay()
Jüri.calculate_pay()