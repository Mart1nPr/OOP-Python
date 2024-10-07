import time

#Stored data
user_data = []

#User data storer
def user_data_storer():
    user_data.append({
        "Username": Username,
        "Password": Password
    })

#Account validation
def account_validation(login_username, login_password):
    for user in user_data:
        if login_username == user["Username"] and login_password == user["Password"]:
            print()
            print("Hello",Username,"!","You entered your account successfully!")
            time.sleep(1)
            print()
            shut_down_input = input("Do you want to close the program? (Y/N): ")
                    
            if shut_down_input == "y" or shut_down_input == "Y":
                shut_down()
            elif shut_down_input == "n" or shut_down_input == "N":
                print()
                print("Okay, you will be redirected to start")
                time.sleep(1)
                break
            else:
                    print("Invalid input")
        print("Wrong login details.")

#Force quit
def shut_down():
        print()
        print("Closed")
        exit()

    
while(True):
    print()
    user_registration_input = input("Do you want to register? (Y/N), Close the program with (Q): ")

    if user_registration_input == "y" or user_registration_input == "Y":
        print()
        Username = input("Create username: ")
        Password = input("Create password: ")
        user_data_storer()
        time.sleep(0.2)
        
    elif user_registration_input == "n" or user_registration_input == "N":
        print()
        print("Sign in")
        user_login_username = input("Username: ")
        user_login_password = input("Password: ")
        account_validation(user_login_username, user_login_password)
        time.sleep(0.2)
    elif user_registration_input == "q" or user_registration_input == "Q":
        shut_down()
    else:
        print()
        print("Invalid")
        time.sleep(1)




