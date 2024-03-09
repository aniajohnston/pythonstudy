''' Conditionals '''

''' Lets follow through the two code snippets below'''

# This will run
x = 20
y = 15

# if x > y:
#     print(x)

# This will not run
x = 20
y = 20

# if x > y:
    # print(x) #there is no result in our terminal



'''
Exercise

Write some code that prints “This is odd” if the user inputs an odd number.
(Hint: use an if statement)
Example:
User input: 7
This is odd
'''

# We can use modulus to figure out odd or even
# val = 6
# result = val % 2
# print(result)


'''Exercise Solution'''
# user_input = int(input('Please enter your number: '))

'''OPTION 1'''
# mod_user_input = user_input % 2

# if mod_user_input == 0:
#     print('Your number is even!')
# if mod_user_input == 1:
#     print('Your number is odd!')

'''IN CLASS: OPTION 2'''

# if user_input % 2 != 0:
#     print('This is odd!')


''' Else If (Elif) Statements '''
'''
We want a small program that will tell a student their grade based on the following scale

A - Between 90 and 100
B - Between 80 and 89
C - Between 70 and 79
D - Between 65 and 69
F - Anything under 65
'''
# get grade from user
# score = int(input('Please enter your grade: '))

#create our conditional
# if score >= 90 and score <=100:
#     print(f'Your score of {score} is an A!')
# elif score >= 80 and score < 90:
#     print(f'Your score of {score} is a B.')
# elif score >= 70 and score < 80:
#     print(f'Your score of {score} is a C.')
# elif score >= 65 and score < 70:
#     print(f'Your score of {score} is a D.')
# else:
#     print(f'Your score of {score} is an F.')



'''Shortening the code - conditions go on either end of our variable'''
# if 90 <= score <=100:
#     print(f'Your score of {score} is an A!')
# elif 80 <= score < 90:
#     print(f'Your score of {score} is a B.')
# elif 70 <= score < 80:
#     print(f'Your score of {score} is a C.')
# elif 65 <= score < 70:
#     print(f'Your score of {score} is a D.')
# else:
#     print(f'Your score of {score} is an F.')



'''Option 3
Why does this work? Because elif is mutually exclusive.
In this code, if always gets run first. If returned False, it moves onto the next elif.'''
# if score >= 90:
#     print(f'Your score of {score} is an A!')
# elif score >= 80:
#     print(f'Your score of {score} is a B.')
# elif score >= 70:
#     print(f'Your score of {score} is a C.')
# elif score >= 65:
#     print(f'Your score of {score} is a D.')
# else:
#     print(f'Your score of {score} is an F.') 

'''If we were to just use 'if' 
Try to input 95 into this code. What happens?'''
# if score >= 90:
#     print(f'Your score of {score} is an A!')
# if score >= 80:
#     print(f'Your score of {score} is a B.')
# if score >= 70:
#     print(f'Your score of {score} is a C.')
# if score >= 65:
#     print(f'Your score of {score} is a D.')
# else:
#     print(f'Your score of {score} is an F.') 
'''When 95 is entered into this code, each if statement runs the code, 
and returns True because 95 >= 65 and >= 70 and >= 80 and >=90'''



'''
Exercise
Add to your previous code so it prints “This is odd” if the user enters an odd number, and “This is even” if the user enters an even number.
(Hint: add an elif statement)

Examples:
User input: 7
This is odd

User input: 12
This is even

'''

''' Exercise solution with an elif and else'''
# user_input = int(input('Please enter your number: '))

#with an elif
# if user_input % 2 != 0:
#     print(f'Your number {user_input} is odd.')
# elif user_input % 2 == 0:
#     print(f'Your number is even.')

#with an else 
'''this works because there is only one other option.'''
# if user_input % 2 != 0:
#     print(f'Your number {user_input} is odd.')
# else user_input % 2 == 0:
#     print(f'Your number is even.')


'''
Exercise
Add to your previous code so if the user enters something that isn't an odd number or an even number, print “Unknown”.


Examples:
User input: 7
This is odd

User input: 12
This is even

User input: 9.2
Unknown

'''

''' Exercise solution(s)'''
# user_input = input('Please enter your number: ') # we know that this is going to be a string.

# if not user_input.isdecimal(): #we use a string method. It will look at a value and see if it 0-9, if nope... 
#     print('Unknown.') #it will print this message.
# elif int(user_input) % 2 != 0: #it will move down here and here is where we neeed to cast to an integer
#     print(f'Your number {user_input} is odd.')   
# else:
#     print(f'Your number {user_input} is even.')


'''Professor's way of solving'''
# try: #tries a line of code
#     user_input = int(input('Please enter your number: ')) #this will get an error if 9.2 is typed.
# except:
#     print('Unknown') #this is the code that you think will break the code and generate the error. This is an error message.
# else:
#     if user_input % 2 != 0: #this is nested
#         print('This is odd')
#     else: #this is nested
#         print('This is even')


'''
Exercise

Write some code that takes in a string from the user and prints whether the string is a number, if it is a word, or something else.

Examples:
User input: 7
This is a number
string method - isdigit

User input: abcde
This is a word
string method -isalpha

User input: 7!ab5
This is something else
else

'''
# user_input = input('Please input your string: ')

# if user_input.isdigit():
#     print('This is a digit')
# elif user_input.isalpha():
#     print('This is a word')
# else:
#     print('This is something else')


'''Chaining Conditionals code results'''

# Mutually exclusive
    
# temp_f = 39
# if temp_f > 70:
#     print("It is hot outside")
# elif temp_f > 40:
#     print("It's moderate outside")
# else:
#     print("It's cold outside")


# result - evaluated separately and multiple of them could be run
# these are not mutually exclusive    
# temp_f = 75
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside")

# 70 won't run because no =70
# temp_f = 70
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40 and temp_f < 70:
#     print("It's moderate outside")
# if temp_f <=40:
#     print("It's cold outside")


# nested conditionals - stacking conditions until it is true
num = 5

# if num % 2 == 1: #checks for odd number #if correct will move to next line
#     if num < 10: #checks if single digit #if correct will move to next line
#         if num > 0: #checks if number is positive #if correct will print:
#             print("This is a single digit odd number")



# if num % 2 and num < 10 and num > 0: #logical operators work like the nested conditionals.
#     print("This is a single digit odd number")


'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''



# Prompt the user to enter their username and password using the input() function. Be sure to sanitize your data.
username = input('Please enter your username: ').strip()

password = input('Please enter your password: ').strip()

# Create two variables called username and password and set them to any valid string values.
real_username = 'ajohns81'
real_password = 'python14*'

# Create your conditional, includes your comparison

if username == real_username and password == real_password:
    print(f'Hello {real_username}, your login was sucessful!')
else:
    print('Incorrect Username or Password')




