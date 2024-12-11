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

print() # Space

# ----Person class----
class Human:
    def __init__(self, name, iq):
        self.__name = name
        self.__iq = iq
    def set_iq(self, new_iq):
        self.new_iq = new_iq
    def get_iq(self):
        return self.__iq
    def details(self):
        print(f"{self.__name} has an iq of {self.__iq}")

person = Human("David", 70)
person.details()
person.set_iq = 80 # Can't change
person.details()   

print() # Space

# ----Tree class----
class Tree:
    def __init__(self, name, height):
        self.__name = name
        self.__height = height
    def set_height(self, new_height):
        self.new_height = new_height
    def get_height(self):
        return self.__height
    def details(self):
        print(f"{self.__name} is {self.__height}m tall")

tree = Tree("Oak", 400)
tree.details()
tree.set_height = 15
tree.get_height()

print() # Space

# ----Employee class----
class Employee:
    def __init__(self, name, position, salery):
        self.name = name
        self.position = position
        self.salery = salery
    def get_status(self):
        print(f"Current status: {self.name} has a position of {self.position} and has a salery of {self.salery}€")
    def update_salery(self, new_salery):
        self.new_salery = new_salery
        if self.new_salery > self.__salery:
            self.__salery = new_salery
        else:
            print("New salery must be higher than old salery")
    def promote(self, new_position, salery_increase):
        self.new_position = new_position
        self.salery_increase = salery_increase
        print(f"You promoted {self.__position} and new salery {self.salery}")

Worker = Employee("John", "Junior-SoftwareDeveloper", 3000)
Worker.get_status()
Worker.update_salery(5000)
Worker.promote("Senior-SoftwareDeveloper", 5000)
Worker.get_status()