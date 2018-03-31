#!/usr/bin/env python3.6
import random
from user import User
from credentials import User_Credentials


def create_credential(acc_name, acc_password):
    '''
    Function to create a new credential
    '''
    new_credential = User_Credentials(acc_name, acc_password)
    return new_credential


def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()


def find_credential(acc_name):
    '''
    Function that finds a credential and returns it
    '''
    return User_Credentials.find_by_name(acc_name)


def check_existing_credentials(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return User_Credentials.find_by_name(name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return User_Credentials.display_credentials()

def main():
    while True:
        print("Welcome to password Locker Application.")
        print('\n')
        print("Use these short codes to select an option: Create New User account use 'cu': Login to your account use 'lg' or 'esc' to exit password locker")
        short_code = input().lower()
        print('\n')

        if short_code == 'cc':
            print("Create your prefered username")
            print("-"*15)
            new_username = input()

            print("Create a desired password")
            print("-"*15)
            new_password = input()

            print("Confirm password")
            confirm_password = input()

            while confirm_password != new_password:
                print("Sorry, passwords inputted did not match! Try again.")
                print("Enter a password")
                new_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {new_username}! You have created your new account.")
                print("-"*20)
                print('\n')
                print("Proceed to your Account")
                print("Username:")
                created_username = input()
                print("Password:")
                created_password = input()

                while created_username != new_username or created_password != new_password:
                    print("You entered a wrong username or password")
                    print("Username:")
                    created_username = input()
                    print("Your Password")
                    created_password = input()
                else:
                    print(f"Welcome: {created_username} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                    print('\n')

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Remove credentials")
                    print("4: Search credentials")
                    print("5: Log Out")
                    option = input()

                    if option == '2':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Account Name")
                                account_name = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    account_password = random.randint(
                                        111111, 1111111)
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_new_credential(create_new_credential(
                                    account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == 'a':
                        while True:
                            print("Your registered accounts are as listed below:")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"ACCOUNT NAME:{credential.acc_name}")
                                    print(f"PASSWORD:{credential.acc_password}")

                            else:
                                print('\n')
                                print("It appears you do not have any accounts yet")
                                print('\n')

                            print("Return to Main Menu? Type y(for yes)/n(for no)")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == 'e':
                        print("WARNING! You will log out of your account. Type y(for yes)/n(for no) to continue...")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out of your account. Goodbye")
                            break
                        elif logout == 'n':
                            continue
                    elif option == 'c':
                        while True:
                            print("Search for account to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                                print("Delete? y(for yes)/n(for no)")
                                proceed = input().lower()
                                if proceed == 'y':
                                    delete_credential(search_credential)
                                    print("Account deleted")
                                    break
                                elif proceed == 'n':
                                    continue

                            else:
                                print("Contact Does not exist")
                                break

                   








