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

    def test_credentials_instance(self):
        '''
        credentails_instance method to test if new credentials have been instantiated correctly.
        '''
        self.assertEqual(self.new_credentials.acc_name,"Fb")
        self.assertEqual(self.new_credentials.acc_password, "12@34")


if __name__ == '__main__':
    unittest.main()
