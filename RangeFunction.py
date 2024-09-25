E = int(input("What do you want to run? "))

match E:
    case 1:
        #Odd numbers
        for i in range(1,21,2):
            print(i)
    case 2:
        #Even numbers
        for i in range(2,21,2):
            print(i)
    case 3:
        #Odd numbers 1 - 100
        for i in range(1, 100):
            if i%3==0:
                print(i)
    case 4:
        #Adding numbers together 1 - 10
        sum = 0
        for i in range(1,11):
            sum = sum + i
        print(sum)
    case 5:
        #Adding all even numbers together 2 - 20
        sum = 0
        for i in range (2, 21, 2):
            sum = sum + i
        print(sum)
    case 6:
        sum = 0
        for i in range(1,51):
            if i%3==0:
                sum = sum + i     
        print(sum)
    
