Runnum = int(input("What do you want to run? "))

match Runnum:
    case 1:
        # Paired numbers
        for i in range(1, 51, 3):
            print(i)
    case 2:
        # Odd numbers
        for i in range(1, 50 ,2):
            print(i)
    case 3:
        # Take an integere input and print even or odd.
        Number = int(input("Enter a number: "))
        if Number%2==0:
            print(Number, "is even.")
        elif Number%3==0:
            print(Number, "is odd.")
        else:
            print("Invalid input.")
    case 4:
        # Print 10 - 1
        for i in range(10, 0, -1):
            print(i)
    case 5:
        # Print 20 - 1
        for i in range(21, 0, -1):
            print(i)
    case 6:
        # Print 10 - 1 in even numbers
        for i in range(10, 0, -1):
            if i%2==0:
                print(i)
    case 7:
        # Print 10 - 1 in odd numbers
        for i in range(10, 0, -1):
            if i%3==0:
                print(i)
    case 8:
        # Add all numbers together from 1 - 100
        sum = 0
        for i in range(1, 101):
            sum = sum + i
        print(sum)
    case 9:
        # Add all numbers together from 1 -100, but the numbers are even
        sum = 0
        for i in range(1, 101):
            if i%2==0:
                sum = sum + i
        print(sum)
    case 10:
        # Add all numbers together from 1 - 100 both even and odd and then add them together
        sum  = 0
        sum2 = 0
        for i in range(1, 100):
            if i%2==0:
                sum = sum + i
            elif i%3==0:
                sum2 = sum2 + i
        print("Even: ", sum, "Odd: ", sum2)
    case 11:
        # Factorial numbers multiplciation 1 * 2 * 3 * 4 * 5
        sum = 1
        for i in range(1,6):
            sum = sum * i
        print(sum)
    case 12:
        # Find number 20 factore numbers
        Number = 20
        for i in range(1, 21):
            if Number%i==0:
                print(i)

                
        


