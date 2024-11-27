# Class "Room"

class Room:
    room_number = 108 # Class Variable

    def __init__(self, item, installed_year, company_name, condition):
        self.item = item
        self.installed_year = installed_year
        self.company_name = company_name
        self.condition = condition

    # Function that returns the details
    def details(self):
        return("Item:{} Year:{} Name:{} Condition:{} Room:{}".format(self.item, self.installed_year, self.company_name, self.condition, self.room_number))

# Items in the room
item1 = Room("Computers", 2024, "Microsoft", "Good")
item2 = Room("Monitors", 2015, "HP", "Old")
item3 = Room("Keyboards", 1999, "Dell", "Dirty")
item5 = Room("Mouse", 1999, "Hp", "Okay")

# Prints items info
print(item1.details())
print(item2.details())
print(item3.details())
print(item4.details())
print(item5.details())
