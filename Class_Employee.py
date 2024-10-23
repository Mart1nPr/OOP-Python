# Class variable & Mstance variable

class Employee:
    nationality = "Estonian" # Class Variable
    num_employee = 0

    def __init__(self, first_name, last_name, salery, background, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.salery = salery
        self.background = background
        self.nationality = nationality

    # Functions that return what we want to see
    def all_data(self):
        return("Name:{} {} Salery:{} Background:{} Nationality:{}".format(self.first_name, self.last_name, self.salery, self.background, self.nationality))
    def name(self):
        return("{} {}".format(self.first_name, self.last_name))
    def sal(self):
        return("{}".format(self.salery))
    def backg(self):
        return("{}".format(self.background))
    def nat(self):
        return("{}".format(self.nationality))

# People
person1 = Employee(first_name="Alex", last_name="Kass", salery=3950, background="CSE")
person2 = Employee(first_name="Brita", last_name="Rahu", salery=1510, background="Math")
person3 = Employee(first_name="David", last_name="Davenson", salery=3510, background="Economist")
person4 = Employee(first_name="Rasmus", last_name="Rahumägi", salery=4200, background="Electronics")

# Print
print(person1.all_data())
print(person2.all_data())
print(person3.all_data())
print(person4.all_data())

