# Encapsulation

class Cars:
    def __init__(self, brand_name, color, speed):
        self.brand_name = brand_name
        self.__color = color # _ Can't change
        self._speed = speed # _ _ Warns, but you can change
    
    def details(self):
        print(f"Brand name {self.brand_name} \n color: {self.__color} \n speed: {self._speed}")

toyota = Cars("Toyota", "Red", 250)

# Old informatiom
print("Old information:")
toyota.details()

# Changed information 
print("New information:")
toyota.color = "Blue"
toyota.speed = 300
toyota.details()
