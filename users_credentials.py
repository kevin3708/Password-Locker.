import random
import string

class User:
    """
    Class that generates new instances of users.
    """
    user_list = []
    def __init__(self,username,password):

        self.username = username
        self.password = password
   
    def save_user(self):
        User.user_list.append(self)
    def delete_user(self):
        User.user_list.remove(self)
    @classmethod
    def user_exists(cls,username,password):
        current_user = ""
        for user in cls.user_list:
            if user.username == username and user.password == password:
                current_user = user.username
                return current_user


class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = []
    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password
       
    def save_credentials(self):
        Credentials.credentials_list.append
    def delete_credentials(self):
        Credentials.credentials_list.remove

  
    def get_random_password(stringLength = 8):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits 
        return ''.join(random.choice(password) for i in range(stringLength))


    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def find_account(cls,account):
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials