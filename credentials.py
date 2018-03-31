class User_Credentials:
    '''
    Class that generates new instances of user credentials for their accounts.
    '''

    list_of_creds = []
    
    def __init__(self, acc_name, acc_password):
        self.acc_name = acc_name
        self.acc_password = acc_password

    