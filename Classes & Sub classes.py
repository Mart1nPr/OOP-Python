# Transport class
class Transport:
    def __init__(self, vehiclename):
        self.vehiclename = vehiclename

    def move(self):
        print(f"{self.vehiclename} is moving")

    def stop(self):
        print(f"{self.vehiclename} is stopping")

class Bus(Transport):
    def public_transport(self):
        print("Tallinn has many public transports")
class Motorcycle(Transport):
    def motobyke(self):
        print("Tallinn has cool motorbikes")
class Bicycle(Transport):
    def bicycles(self):
        print("Tallinn has a lot of bikers")
class Car(Transport):
    def CarType(self):
        print(f"{self.vehiclename} is very good car")
    def CarPay(self):
        print("I hate car payments!!!")

Bus1 = Transport("Iveco")
Motorcycle1 = Motorcycle("Motorcycle")
Bicycle1 = Bicycle("Bicycle")
Car1 = Car("BMW E30 325i")

print()
print("Car")

Car1.CarType()


# Person class
class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
    def AllDetails(self):
        print(f"Name:{self.name} Age:{self.age} Profession:{self.profession}")
    def PersonsName(self):
        print(f"Name: {self.name}")
    def PersonsAge(self):
        print(f"Age: {self.age}")
    def PersonsProfession(self):
        print(f"Profession: {self.profession}")

class Father(Person):
    pass
class Mother(Person):
    pass
class Son(Person):
    pass

father = Father("Andrus", 45, "Mechanic")
mother = Mother("Anna", 43, "Libearian")
son = Son("Rauno", 15, "Quitar player")

print()
print("Person")

father.AllDetails()
mother.AllDetails()
son.AllDetails()


# Shape class
class Shape:
    def __init__(self, dim1, dim2) -> None:
        self.dim1 = dim1
        self.dim2 = dim2

class Square(Shape):
    def square_area(self):
        area = self.dim1 * self.dim1
        print("Area of this square is:", area)

class Circle(Shape):
    def circle_area(self):
        area = 3.14 * self.dim1 * self.dim1
        print("Area of circle is:", area)

    def circle_perimeter(self):
        perimeter = 2 * 3.14 * self.dim1
        print("Perimeter of circle is:", perimeter)

class Rectangle(Shape):
    def rectangle_area(self):
        area = self.dim1 * self.dim2
        print("Area of rectangle is:", area)

    def rectangle_perimeter(self):
        perimeter = 2 * (self.dim1 + self.dim2)
        print("Perimeter of rectangle is:", perimeter)

class Triangle(Shape):
    def triangle_area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle is:", area)

    def triangle_perimeter(self, side3):
        perimeter = self.dim1 + self.dim2 + side3
        print("Perimeter of triangle is:", perimeter)


print()
print("Shapes")

square = Square(5, 0)  

circle = Circle(3, 0)
circle.circle_area()
circle.circle_perimeter()

rectangle = Rectangle(4, 6)
rectangle.rectangle_area()
rectangle.rectangle_perimeter()

triangle = Triangle(4, 5) 
triangle.triangle_area()
triangle.triangle_perimeter(6)


# Calculation class
class calculation:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class calculation1(calculation):
    def calculation1(self):
        result = self.a + self.b + self.c + self.d
        print(f"{self.a} + {self.b} + {self.c} + {self.d} = ", result)
class calculation2(calculation):
    def calculation2(self):
        result = self.a - self.b + self.c - self.d
        print(f"{self.a} - {self.b} + {self.c} - {self.d} = ", result)
class calculation3(calculation):
    def calculation3(self):
        result = self.a * self.b + self.c / self.d
        print(f"{self.a} * {self.b} + {self.c} / {self.d} = ", result)
class calculation4(calculation):
    def calculation4(self):
        result = self.a / self.b + self.c * self.d
        print(f"{self.a} / {self.b} + {self.c} * {self.d} = ", result)

Calculation1 = calculation1(1, 2, 3, 4)
Calculation2 = calculation2(1, 2, 3, 4)
Calculation3 = calculation3(1, 2, 3, 4)
Calculation4 = calculation4(1, 2, 3, 4)

print()
print("Calculation")

Calculation1.calculation1()
Calculation2.calculation2()
Calculation3.calculation3()
Calculation4.calculation4()


# Animal class
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

fish = Fish("Kala")
rabbit = Rabbit("Jänes")
hawk = Hawk("Kotkas")

print()
print("Animal")

fish.hunt()
fish.flee()
fish.eat()
fish.sleep()
hawk.hunt()
hawk.eat()
hawk.sleep()
rabbit.flee()
rabbit.eat()
rabbit.sleep()

# Calculation class2 
class calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        sum = self.a + self.b
        print("Sum is ", sum)
class calculation1(calculation):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d
    def add1(self):
        sum = self.a + self.b + self.c +self.d
        print(f"{self.a} + {self.b} + {self.c} + {self.d} = ", sum) 
class calculation2(calculation1):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c ,d)
        self.e = e
    def add2(self):
        sum = self.a +self.b + self.c + self.d + self.e
        print(f"{self.a} + {self.b} + {self.c} + {self.d} + {self.e} = ", sum)
class calculation3(calculation2):
    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c, d, e)
        self.f = f
    def add3(self):
        sum = self.a +self.b + self.c + self.d + self.e + self.f
        print(f"{self.a} + {self.b} + {self.c} + {self.d} + {self.e} + {self.f} = ", sum)

cal1 = calculation1(1, 2, 3, 4)
cal2 = calculation2(1, 2, 3, 4, 5)
cal3 = calculation3(1, 2, 3, 4, 5, 6)

print()
print("Calculation2")

cal1.add1()
cal2.add2()
cal3.add3()


# Human class
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
class Einstein(Human):
    def __init__(self, name, age, height, iq):
        super().__init__(name, age, height)
        self.iq = iq
    def EinsteinData(self):
        print("About Einsetin:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")
        print(f"  Height: {self.height}")
        print(f"  IQ: {self.iq}")
class Alex(Human):
    def __init__(self, name, age, height, is_smart):
        super().__init__(name, age, height)
        self.is_smart = is_smart
    def AlexData(self):
        print("About Alex:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")
        print(f"  Height: {self.height}")
class Newton(Human):
    def __init__(self, name, age, height, formula):
        super().__init__(name, age, height)
        self.formula = formula
    def NewtonData(self):
        print("About Einsetin:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")
        print(f"  Height: {self.height}")
        print(f"  Formula: {self.formula}")

einstein = Einstein("Albert", 79, 170, 145)
alex = Alex("Alex", 17, 178, "is very smart guy")
newton = Newton("Newton", 80, 170, "formula")

print()
print("Human")

einstein.EinsteinData()
alex.AlexData()
newton.NewtonData()

# Human class2

class human:
    def __init__(self, name, age, IDnumber , salery):
        self.name = name
        self.age = age
        self.IDnumber = IDnumber
        self.salery = salery
class boy(human):
    def __init__(self, name, age, IDnumber, salery, bonus):
        super().__init__(name, age, IDnumber, salery)
        self.bonus = bonus
    def totalsalery(self):
        totalsalery = self.salery + self.bonus
        print(f"{self.name}: ",totalsalery)
class girl(human):
    def __init__(self, name, age, IDnumber, salery, tips):
        super().__init__(name, age, IDnumber, salery)
        self.tips = tips
    def totalsalery(self):
        totalsalery = self.salery + self.tips
        print(f"{self.name}: ",totalsalery)

Boy  =  boy("Arnold", 19, 5052280226, 2500, 100)
Girl = girl("Anna", 20, 6052280236, 1240, 50)

print()
print("Human 2")

Boy.totalsalery()
Girl.totalsalery()