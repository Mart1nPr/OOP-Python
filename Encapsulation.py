# Encapsulation

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

# Exercise
class Person:
    def __init__(self, name, age):
        self.__name = name # Can't change the name
        self.__age = age # Can't change the age
    
    def personalData(self):
        print(f"Name: {self.__name} \n Age: {self.__age}")

David = Person("David", 69)
print("Old information")
David.personalData()
David.__name = "John" # Name change
David.__age = 420 # Age change
David.personalData()