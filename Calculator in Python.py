#Simple calculator in Python

import time

while(True):
    Operator = input("Enter an operator to do math with (+ - * /) Use ( . ) to exit: ")

    if Operator == ".":
        print("Closed")
        break
    if Operator not in ["+", "-", "*", "/"]:
        print("You entered an invalid operator.")
    else:
        Num1 = int(input("Enter your first number: "))
        Num2 = int(input("Enter a second number: "))

        if Operator == "+":
            Result = Num1 + Num2
        elif Operator == "-":
            Result = Num1 - Num2
        elif Operator == "*":
            Result = Num1 * Num2
        elif Operator == "/":
            Result = Num1 / Num2

        print(Num1, Operator, Num2, "=", Result)
        time.sleep(1)
