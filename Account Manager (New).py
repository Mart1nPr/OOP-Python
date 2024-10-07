# This version of the account manager actually works!
# Feel free to test it out!

import time

# Stored data
user_data = []

#User data storer
def user_data_storer():
    user_data.append({
        "Username": Username,
        "Password": Password
    })

# Account validation
def account_validation():
    while True:
        user_login_username = input("Username: ")
        user_login_password = input("Password: ")
        if user_login_username == Username and user_login_password == Password:
            print()
            print("Hello", Username, "!", "You entered your account successfully!")
            time.sleep(1)
            print()
            shut_down_input = input("Do you want to close the program? (Y/N): ")

            if shut_down_input == "y" or shut_down_input == "Y":
                shut_down()
            elif shut_down_input == "n" or shut_down_input == "N":
                print()
                print("Okay, you will be redirected to start")
                time.sleep(1)
                return
            else:
                print("Invalid input")

        else:
            # No matching user found
            print()
            print("Wrong login details.")
            time.sleep(1)
            print()
            while True:
                login_retry = input("Do you want to try logging in again? (Y/N): ")
                if login_retry == "y" or login_retry == "Y":
                    print()
                    break
                elif login_retry == "n" or login_retry == "N":
                    return
                else:
                    print()
                    print("Invalid")
                    time.sleep(1)
                    print()
           

#Force quit
def shut_down():
        print()
        print("Closed")
        exit()

# Main   
while True:
    print()
    user_registration_input = input("Do you want to register? (Y/N), Close the program with (Q): ")

    if user_registration_input == "y" or user_registration_input == "Y":
        print()
        Username = input("Create username: ")
        Password = input("Create password: ")
        user_data_storer()
        print()
        print("Account successfully created!")
        time.sleep(1)
        print()
        
    elif user_registration_input == "n" or user_registration_input == "N":
        print()
        print("Sign in")
        account_validation()
        time.sleep(0.2)
    elif user_registration_input == "q" or user_registration_input == "Q":
        shut_down()
    else:
        print()
        print("Invalid")
        time.sleep(1)
        print()




