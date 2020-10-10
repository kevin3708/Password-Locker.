from users_credentials import User,Credentials
def create_user(username,password):
    new_user = User(username,password)
    return new_user
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()

def create_credentials(account,username,password):
    new_credentials = Credentials(account,username,password)
    return new_credentials
def save_credentials(credentials):
    credentials.save_credentials()
def delete_credentials(credentials):
    credentials.delete_credentials()
def get_random_password():
    p_word = Credentials.get_random_password()
    return p_word


def main():
    print("Hello welcome to your password locker. What would you like to do?")
    print("use these short codes: cu - create a new username, du - delete a username, cc - create new credentials, dc - delete credentials, ex -  exit the password locker")
    short_code = input().lower()

    if short_code == 'cu':
        print("New Username")
        username = input(' Enter username: ')
        
        while True:
            print('use : cc = to auto generate a password for your account')
            user_option = input().lower()
            if user_option == 'cc':
                password = get_random_password()
                break
            else:
                print('Invalid short code')
                
            save_user(create_user(username,password))
            print('New username created, your password is {password} ')
       
  
    elif short_code == 'du':
        print("Enter the username you wish to delete")
        del_user = input()
        if delete_users(del_user):
            User.user_list.remove(User)
       
        else:
            print("That user does not exist")
      
    if short_code == 'cc':
        print("Create new Credentials: ")
        account = input('Which acccount:')
        username  = input('Username for this account:')
        password = input('New password:')
        
        
        save_credentials(create_credentials(account,username,password))
        print("New Passwords created.")
    elif short_code == 'dc':
        print("Enter the credentials you wish to delete")
        del_credentials = input()
        if delete_credentials(del_credentials):
            Credentials.credentials_list.remove(Credentials)
        
        else:
            print("Those credentials do not exist")
          
    
        if short_code == 'ex':
            print("Goodbye")
    
     
        else:
            print("I didn't get that, please use the short codes")
   
        
if __name__ == '__main__':
    main()
