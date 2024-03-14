import re #import regular expression library right at the top of your code


''' What are some of the things we may come across while building this project'''

'''Initialization and prompt (and testing)'''
first_input, second_input = '','' #initialization for username and password

# while True:
#     first_input = input('Please enter your data')
#     second_input = input('Please enter your data')
#     print(first_input,second_input)
#     break

'''Handling error messages with a list (and testing)'''

error_messages = ['Error message 1','Error message 2', 'This is my error message']
# at any point in your program you can access these with a print statement

# if 5 > 7:
    # print(error_messages[0])
# else:
    # print(error_messages[2])

'''Testing a string'''

# Example of string testing (testing for lowercase letter)
test_string = 'Popeye1989'

# Testing for uppercase as first letter
first_letter = test_string[0]
lower_case_test = first_letter.islower()

# if lower_case_test:
#     print('This string passed lowercase testing')
# else:
#     print('This string failed lower case testing.')



''' Taken usernames '''
sample_word = 'blue'
sample_list = ['green','blue','orange','yellow','purple']

# if sample_word in sample_list:
#     print('Word exists in the list')
# else:
#     print("Word does not exist in list")


''' Using Break and Continue to control the follow of loop'''

# If input is a number we will go through this while loop and continue through, if not, we will send the user back to the beginning

# while True:
#     userinput = input('What is your test string? ')
#     if userinput.isnumeric():
#         print("This is a number, we will stay in the loop")
#     else:
#         print("Not a number, have the user try again")
#         continue

#     print("if you see this line of code, you are still in the loop")
#     break


''' Password requirements '''
test_string_2 = 'c1234567'

# At least 8 characters long


# Contains at least one uppercase letter
#integrating the for loop with a condition
one_uppercase = False
for t in test_string_2:
    if t.isupper(): #don't mess this up
        one_uppercase = True
# print('Contains at least one uppercase letter?', one_uppercase)


# Even better, is the any function! Tests if any of items in iterable is true
# any_uppercase = any(u.isupper() for u in test_string_2) #ONE LINE OF CODE
# print('Contains at least one uppercase letter?', any_uppercase)

# Or Regular Expressions match method

#casting it all to a Boolean # re calls regular expression #. brings up methods #match pattern
uppercase_test_regex = bool(re.match(r'\w*[A-Z]\w*', test_string_2)) 
# print('Contains at least one uppercase letter?', uppercase_test_regex)
#identifies patterns


''' Logging in and handling the loop'''

# These can represent the user id and password the user created let's say these follow the given rules
sys_username = 'simonsays123'
sys_password = 'fido1950'


# These can represent the re-authentication. Here we will prompt them again
username = 'simonsays123'
password = 'fido1950'

# Lets check for a match

while True:
    if sys_username == username and sys_password == password:
        print('Login Sucessful')
        break
    else:
        print('Incorrect username and password')
        continue
'''Hey Ania, you finally answered the same as the professor! YAY!!!'''