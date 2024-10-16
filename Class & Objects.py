class Employee:
    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    def email_details(self):
        return "{}.{}".format(self.first, self.last + "@gmail.com")

Janitor = Employee(first = "Alex", last = "Kass", age = 35, pay = 750)
Teacher = Employee(first = "Allar", last = "Veelmaa", age = 65, pay = 2500)

print(Janitor.email_details())
