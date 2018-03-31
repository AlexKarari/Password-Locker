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


