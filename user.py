class User:
    """
    Class that generates new instances of users.
    """
    def __init__(self, user_name,gender, password):
        self.user_name = user_name
        self.gender = gender
        self.password = password

    list_of_users = []

    