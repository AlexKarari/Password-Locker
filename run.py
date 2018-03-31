#!/usr/bin/env python3.6
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

                   







