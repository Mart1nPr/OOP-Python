# Types of numbers

E = int(input("What code do you wish to run? (1 - 3): "))

match E:
    case 1:
        # Spy number

        num = int(input("Enter your number: "))
        sum = 0
        prod = 1

        while num != 0:
            rem = num%10
            sum = sum + rem
            prod = prod * rem
            num = num // 10
        if sum == prod:
            print("Spy number")
        else:
            print("Not an spy number")
    case 2:
        # Duck number

        num = int(input("Enter a number: "))
        count = 0
        while num != 0:
            rem = num%10
            if rem == 0:
                count += 1
            num = num//10
        if count > 0:
            print("Duck number")
        else:
            print("Not a duck number")
    case 3:
        # Neon number
        
        num = int(input("Enter a number: "))
        sum = 0
        Square = num * num
        while Square != 0:
            remain = Square%10
            sum = sum + remain
            Square = Square // 10
        if sum == num:
            print(num, "is a neon number")
        else:
            print(num, "is not neon number")
