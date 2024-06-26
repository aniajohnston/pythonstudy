import re

'''Project Description: Website Sign-Up'''

'''Write a program that prompts the user to sign up for a website. 
The user must come up with a username and password, then log in.
'''

'''USERNAME REQUIREMENTS'''
'''The username must:
Follow all the Python conventions for a variable name.
1. It must start with a lowercase letter
2.It must only contain letters, numbers, and underscores.
3.It must not be in the list of taken usernames:
Taken usernames = "admin", "admin123", "superuser", "superuser123"
If the username does not meet these requirements, print:
"Invalid Username" or "Username Taken" and continue looping

The password must:
1. Be at least 8 characters long
2. Contain at least one uppercase letter
3. Contain at least one lowercase letter
4. Contain at least one digit
5. Contain at least one of these characters: !,?,@,#,$,^,&,*,_,-
6. Cannot contain any spaces
'''

#initialization
username, password = '',''

#lists 
error_messages = ['Invalid Username:','Username Taken:', 'Invalid Password:', 'Sign up sucessful!', 'Incorrect Username or Password:', 'Login sucessful!']
taken = ['admin', 'admin123', 'superuser', 'superuser123']


while True:
    #username
    username = input('\nPlease enter your username.\nIt must start with a lowercase letter.\nIt must follow python conventions(only contain letters, numbers, and underscores).\nIt must not be in the list of taken usernames:\n\n\t"admin", "admin123", "superuser", "superuser123"\n\nUsername: ')
    
    #must start with a lowercase letter
    first_letter = username[0]
    lower_case_test = first_letter.islower()
    if lower_case_test:
        print(f'Test Passed: {username} starts with a lowercase letter.')
    
    else:
        print(f'{error_messages[0]} {username} does not start with a lowercase letter.')
        continue

    #contains letters, numbers, underscores
    py_conventions = bool(re.match("^[A-Za-z0-9_-]*$", username))
    if py_conventions:
        print(f'Test Passed: {username} follows python conventions.')
    else:
        print(f'{error_messages[0]} {username} does not follow python conventions.')
        continue

    #must not be in the list of taken usernames
    if username not in taken:
        print(f'Test Passed: {username} is not in the list of taken usernames.')
    else:
        print(f'{error_messages[1]} {username} is in the list of taken usernames.')
        continue

    #password
    password = input('\nPlease enter your password.\nIt must be at least 8 characters long.\nIt must contain at least one uppercase letter.\nIt must contain at least one lowercase letter.\nIt must contain at least one digit.\nIt must contain no spaces.\nIt must contain a special character from this list:\n\n!?@#$^&*_-\n\nPassword:')

    #must be at least 8 characters long
    if len(password) >= 8:
        print(f'Test Passed: {password} is greater than 8 characters')
    else:
        print(f'{error_messages[2]} {password} is less than 8 characters')
        continue

    #must contain at least one uppercase
    one_uppercase = any(u.isupper() for u in password) # will deliver True False if capital happens in the string
    if one_uppercase:
        print(f'Test Passed: {password} contains a capital letter')
    else:
        print(f'{error_messages[2]} {password} contains no capital letters')
        continue
    
    #must contain at least one lowercase
    lowercase_test = bool(re.match(r'^.*[a-z].*$', password))
    if lowercase_test:
        print(f'Test Passed: {password} contains a lowercase')
    else:
        print(f'{error_messages[2]} {password} does not contain a lowercase')
        continue

    #must contain at least one digit
    contains_num = re.search(r'\d', password) 
    if contains_num:
        print(f'Test Passed: {password} contains a number')
    else:
        print(f'{error_messages[2]} {password} does not contain a number')
        continue
    
    #special characters
    special_characters = re.compile('[!?@#$^&*_-]')
    if(special_characters.search(password) != None):
        print(f'Test Passed: {password} contains special characters')
    else:
        print(f'{error_messages[2]} {password} does not contain special characters')
        continue

    #no spaces
    space = re.search(r'\s', password)
    if not space:
            print(f'{error_messages[2]} {password} does not contain a space')
            print(f'{error_messages[3]}')
    else:
        print(f'{error_messages[2]} {password} contains a space')
        continue
    
    #reauthentication
    sys_username = input('Please type in your username for reauthentication: ')
    sys_password = input('Please type in your password for reauthentication: ')

    
    if sys_username == username and sys_password == password:
        print(f'{error_messages[5]}')
        break
    else:
        print(f'{error_messages[4]}')
        continue
