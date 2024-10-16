# Functions in python

def addsum(num1, num2):
    sum = num1+num2
    avarage = sum / 2
    return sum, avarage

print(addsum(num1=20, num2=30))

# Takes in a number and then outputs an factorial number of that number.
num = int(input("Enter a number: "))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(num, "in factorial is:", fact)

factorial(num)
