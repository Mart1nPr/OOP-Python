num = int(input("Enter your number: "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuseday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thirsday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Your input was wrong")