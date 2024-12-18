# Aggregation

# First exercise
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def details(self):
        print(f"Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} added to {self.name} department.")
        
    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for emp in self.employees:
            emp.details()

employee1 = Employee("Alex", "Software Developer")
employee2 = Employee("David", "Data Analyst")
department = Department("Software Development")
department.add_employee(employee1)
department.add_employee(employee2)
print()
print("Software Development Team:")
department.list_employees()

# Second exercise
class Professor:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def professor_details(self):
        print(f"Name: {self.name}, Department: {self.department}")

class University:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)
        print(f"{professor.name} added to {self.name}.")
        
    def list_professors(self):
        print(f"Professors in {self.name}:")
        for prof in self.professors:
            prof.professor_details()

professor1 = Professor("Alex", "Physics")
professor2 = Professor("David", "Mathematics")
university = University("School 123")
university.add_professor(professor1)
university.add_professor(professor2)
print()
print("University Professors:")
university.list_professors()

# Third exercise
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def player_details(self):
        print(f"Name: {self.name}, {self.position}")

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
        print(f"{player.name} added to {self.name} team.")
        
    def list_players(self):
        print(f"Players in {self.name} team:")
        for player in self.players:
            player.player_details()

player1 = Player("Alex", "Attack")
player2 = Player("David", "Defense")
team_red = Team("Red")
team_blue = Team("Blue")
team_red.add_player(player1)
team_blue.add_player(player2)
print()
print("Sports Teams:")
team_red.list_players()
team_blue.list_players()

# Fourth exercise 