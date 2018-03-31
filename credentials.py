class User_Credentials:
    '''
    Class that generates new instances of user credentials for their accounts.
    '''

    list_of_creds = []

    def __init__(self, acc_name, acc_password):
        self.acc_name = acc_name
        self.acc_password = acc_password

    def save_credentials(self):
        '''
        save credentials method that stores new credentials into list_of_creds
        '''
        self.list_of_creds.append(self)

    def delete_credentials(self):
        '''
        delete_contact method deletes a saved credential from the list_of_creds
        '''

        User_Credentials.list_of_creds.remove(self)

    @classmethod
    def find_by_name(cls, acc_name):
        '''
        Method that takes in a name and returns a credential that matches that number.

        Args:
            name: acc_name to search for
        Returns :
            The acc_name and its password
        '''

        for credential in cls.list_of_creds:
            if credential.acc_name == acc_name:
                return credential

    