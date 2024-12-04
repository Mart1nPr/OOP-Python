# Encapsulation

# ----Cars class----
class Cars:
    def __init__(self, brand_name, color, speed):
        self.brand_name = brand_name
        self.__color = color # _ Can't change
        self._speed = speed # _ _ Warns, but you can change
    
    def details(self):
        print(f"Brand name: {self.brand_name} \n color: {self.__color} \n speed: {self._speed}")

toyota = Cars("Toyota", "Red", 250)

# Old informatiom
print("Old information")
toyota.details()

# Changed information 
print("New information")
toyota.color = "Blue"
toyota.speed = 300
toyota.details()

print() # Space

# ----Person class----
class Person:
    def __init__(self, name, age):
        self.__name = name # Can't change the name
        self.__age = age # Can't change the age
    
    def personalData(self):
        print(f"Name: {self.__name} \n Age: {self.__age}")

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.__gpa = gpa # Can't change the gpa
    def studentData(self):
        print(f" GPA: {self.__gpa}")


David = Person("David", 69)
David = Student("David", 69, 100)
print("Old information")
David.personalData()
David.studentData()

print() # Space

David.__name = "John" # Name change
David.__age = 420 # Age change
David.__gpa = 101 # Gpa change
print("New information")
David.personalData()
David.studentData()

print() # Space

# ----Rice class----
class Rice_Price:
    def __init__(self, company_name, price):
        self.company_name = company_name
        self.__final_price = price +price * 0.1
        self.price = price
    
    def set_final_price(self, discount):
        self.discount = discount
        self.__final_price = self.__final_price - self.__final_price*(self.discount/100)
    
    def get_final_price(self):
        return self.__final_price

rice = Rice_Price("ABC", 5) # Company name & price
rice.set_final_price(20) # Procentage of discount %
print("Discount price: ",rice.get_final_price())