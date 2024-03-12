


error_messages = ['Invalid username','Username taken', 'Invalid password', 'Sign up sucessful', 'Incorrect username or password', 'Login sucessful']
characters = ['!','?','@','#','$','^','&','*','_','-']

username = ''
password = ''
taken = ['admin', 'admin123', 'superuser', 'superuser123']


while True:
    username = input('f\nPlease type your username.\n It must start with a lowercase\n only contain letters, numbers, and underscores\n Taken usernames are: {taken}\n\n USERNAME:')
    password = input(f'\nPlease type your password.\n It must contain at least 8 characters\n at least one uppercase letter\n at least one lowercase letter\n at least one digit\n one of these characters:{characters}\n cannot contain spaces \n\n PASSWORD:')
    #the username must not be in the list of taken usernames
    if username.capitalize():
          print('Your username must not have a capital')
          break
    elif username in taken:
            print(username, error_messages[1])
            break
'''username requirements:
no spaces
must start with a lowercase letter
only contain letters
only contain numbers
only use underscores
'''
#not be in the list of taken usernames


'''password requirements:
at least 8 characters long
at least one uppercase letter
at least one lowercase letter
at least one digit
contain at least one special characters
doesn't contain spaces
'''



#password contains at least one special character
# for p in password:
#     if p in characters:
#         continue