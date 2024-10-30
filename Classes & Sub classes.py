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