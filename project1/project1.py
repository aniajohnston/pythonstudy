


taken_username = ['admin', 'admin123', 'superuser', 'superuser123']
error_messages = ['Invalid username','Username taken', 'Invalid password', 'Sign up sucessful', 'Incorrect username or password', 'Login sucessful']
characters = ['!','?','@','#','$','^','&','*','_','-']

username = ''
password = ''


while True:
    username = input(f'\nPlease type your username.\n It must start with a lowercase\n only contain letters, numbers, and underscores\n Taken usernames are: {taken_username}\n\n USERNAME:')
    password = input(f'\nPlease type your password.\n It must contain at least 8 characters\n at least one uppercase letter\n at least one lowercase letter\n at least one digit\n one of these characters:{characters}\n cannot contain spaces \n\n PASSWORD:')

'''username requirements:
no spaces
must start with a lowercase letter
only contain letters
only contain numbers
only use underscores
not be in the list of taken username
'''


'''password requirements:
at least 8 characters long
at least one uppercase letter
at least one lowercase letter
at least one digit
contain at least one special characters
doesn't contain spaces
'''

