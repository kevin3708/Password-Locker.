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
def display_credentials():
    return Credentials.display_credentials()
def find_account(account):
    return Credentials.find_account(account)
def check_user(username,password):
    checked = User.user_exists(username,password)
    return checked
def get_random_password():
    p_word = Credentials.get_random_password()
    return p_word


def main():
    print("Hello welcome to your password locker. Please enter your name")
    username = input()
    print("Welcome")
    print('\n')

    while True:
        print("use these short codes: cu - create a new username, du - delete a username, cc - create new credentials, dc - display credentials,du - delete an account,lg - log into your account, ex -  exit the password locker")
        short_code = input().lower()

        if short_code == 'cu':
            print("New Username")
            create_username = input(' Enter username: ')
            print("Create password")
            create_password = input('Password :')
            print("Confirm Password")
            confirm_password = input('Password confirm: ')

            if create_password == confirm_password:
                save_user(create_user(create_username,create_password))
                print("New user created")

            else:
                print("I did not recognize that.")
            

        elif short_code == 'lg':
            print("Enter your username and password")
            entered_username = input('Enter username: ')
            entered_password = input('Enter password: ')
            verify = check_user(entered_username,entered_password)

            if entered_username == verify :
                print(f"Welcome {entered_username} to your account.Use the short codes as described to continue")

            else:
                print("You don't seem to have an account with us")
        
        
        elif short_code == 'cc':
            print("Enter the account for which you wish to create credentials")
            created_account = input('Which account: ')

            print("Enter account username")
            account_username = input('Enter account username: ')
            while True:
                print("If you wish to create your password use 'cp'.To have it generated for you use 'gp'")
                user_choice = input('How do you wish to proceed?: ')
                if user_choice == 'cp':
                    password = input('Enter passcode: ')
                    break
                elif user_choice == 'gp':
                    password = get_random_password()
                    break

            save_credentials(create_credentials(created_account,account_username,password))


        elif short_code == 'du':
            print("Enter account to delete")
            search_for_account = input('Enter the account: ')
            if find_account(search_for_account):
                account_found = find_account(search_for_account)
                account_found.delete_credentials()
                print("Account deleted")

       
            else:
                print("That account does not exist")
      
        elif short_code == 'dc':

            if display_credentials():
                print("This is a list of your credentials")
                for credential in display_credentials():
                    print(f"Account_name: {credential.account} Username: {credential.username} Password: {credential.password}")

            else:
                print("You have not yet created an account with us")


          
    
        elif short_code == 'ex':
            print("Goodbye")
            break
    
     
        else:
            print("I didn't get that, please use the short codes")
   
        
if __name__ == '__main__':
    main()
