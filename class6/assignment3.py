'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''



# prompts the user to enter their username and password using the input() function and sanitizes
username = input('Please enter your username: ').strip() #auto-clean data

password = input('Please enter your password: ').strip() #auto-clean data

# two variables called username and password  set to specific strings.
real_username = 'ajohns81' #username string
real_password = 'python14*' #password string

# conditional with the comparison
if username == real_username and password == real_password: #comparison
    print(f'Hello {real_username}, your login was sucessful!') #output if sucessful
else:
    print('Incorrect Username or Password') #output if failed
