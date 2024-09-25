Operator = input("Enter an operator: (+ - * /): ")
A = int(input("Enter your first number: "))
B = int(input("Enter a second number: "))

match Operator:
    case "+":
        Math = A + B
        print("Answer is: ", Math)
    case "-":
        Math = A - B
        print("Answer is: ", Math)
    case "*":
        Math = A * B
        print("Answer is: ", Math)
    case "/":
        Math = A / B
        print("Answer is: ", Math)
    case _:
        print("Your input was wrong")