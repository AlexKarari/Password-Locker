import unittest
from credentials import User_Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user_credentials class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = User_Credentials("Fb", "12@34")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.acc_name,"Fb")
        self.assertEqual(self.new_credentials.acc_password, "12@34")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the list_of_creds
        '''
        self.new_credentials.save_credentials()  # saving the new credentials
        self.assertEqual(len(User_Credentials.list_of_creds), 1)

if __name__ == '__main__':
    unittest.main()
