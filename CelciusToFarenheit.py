Enterance = int(input("Enter 1 - Celcius, 2 - Fahrenheit: "))

match Enterance:
    case 1:
        C = int(input("Enter a Celcius value: "))
        F =  C * (9/5) + 32
        print("In fahrenheit it is: ", F)
    case 2:
        F = int(input("Enter an Fahrenheit value: "))
        C = (F-32) * 5/9
        print("In celcius it is: ", C)
