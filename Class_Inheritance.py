class Animal:
    def __init__(self, name, alive):
        self.name = name
        self.alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def character(self):
        print(f"{self.name} is faithful")
class Cat(Animal):
    def look(self):
        print(f"{self.name} is beautiful to look at")

dog1 = Dog("Toni", True)
dog1.eat()
dog1.sleep()
dog1.character()

cat1 = Cat("Garfield", True)
cat1.eat()
cat1.sleep()
cat1.look()


