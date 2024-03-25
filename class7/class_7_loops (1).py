''' Loops '''

''' While Loops '''

# value = 1

'''issue #1'''
# while value <= 10:
#     if value == 5:
#         continue
#     print(value)
#     value += 1 # never get executed, loop pauses at 5

'''issue #2'''
# while value <= 10:
#     value += 1
#     print(value) #loop prints 5 before 
#     if value == 5: #skipping 5
#         continue

'''issue #3'''
# while value <= 10:
#     print(value) 
#     if value == 5: 
#         continue
#     value += 1 # creates an infinite loop
'''when value becomes 5, 'continue' sends the value back to the top
and incriment never gets executed printing infinte '5' '''

'''issue #4'''
# while value <= 10:
#     if value == 5:
#         continue
#     value += 1 
#     print(value)
'''Let's walk through the code when value is 5:
value is 5.
The if condition if value == 5: is true.
The continue statement is executed, which causes the 
loop to skip to the next iteration without executing the rest of 
the loop body.
The loop condition while value <= 10: is re-evaluated. 
Since value remains 5 and the loop condition is still satisfied, 
the loop continues.
However, since the continue statement is encountered every time 
value equals 5, the loop never gets a chance to execute 
value += 1 after value is incremented to 5, and it remains 
stuck in an infinite loop.'''

'''correct method'''
# while value <= 10:
#     value += 1 
#     if value == 5:
#          continue
#     print(value)

'''STRING INITIALIZATION NOTES'''
# # Initializing an empty string

# user_input = ''
# # Prompting the user for input until they enter 'quit'
# while user_input != 'quit':
#     user_input = input("Enter a value (type 'quit' to exit): ")
#     # Perform operations based on user input
#     print("You entered:", user_input)
    
# print("Exiting the loop.")


# # Prompting the user for input before the while loop
# user_input = input("Enter a value (type 'quit' to exit): ")

# # Entering the while loop
# while user_input != 'quit':
#     # Perform operations based on user input
#     print("You entered:", user_input)
    
#     # Prompting the user for input inside the loop
#     user_input = input("Enter a value (type 'quit' to exit): ")

# print("Exiting the loop.")


"""print comes after +="""
# x = 0
# while x < 5:
#     x += 1  # Increment x by 1
#     print("Current value of x:", x)  # Print the updated value of x
#12345

# """print comes before +="""
# x = 0
# while x < 5:
#     print("Current value of x:", x)  # Print the current value of x
#     x += 1  # Increment x by 1
#01234


''' While my start value is less than my end value, we will increment by 1'''
# end = int(input('Please enter your number: '))
# start = 0

# while start < end:
#     print(start)
#     start += 1
# starts at zero and ends at 24 if our input value is 25 because we use <
# asks is 25 < 25, condition fails and it stops.

''' While my start value is less than my end value, we will decrement by one - You can stop the infinite loop by hitting ctrl + c'''
# end = 20
# start = 0

# while start < end:
#     print(start)
#     start -= 1

#make sure to hit ctrl c in terminal

''' Example Create a while loop that prints every integer from 1 to 10.'''
# end = 11 #initialization
# start = 1

# while start < end: #condition
#     print(start)
#     start += 1


'''
While Loops and User Input

While loops are often paired with user input. The condition for the loop might be what the user needs to enter to stop the loop. The user is prompted for input each time it loops, and something happens based on that input.
This allows you to take user input multiple times without writing multiple lines of input(). It also allows the user to control how much input they give.

Lets look at code that will run infinitely until the user tells it to "stop"
'''

# initialize our string
# userin = ''

# while userin != 'stop' :
#     userin = input("Please enter a word, or 'stop' to end the loop: ")
#     print(userin)
#we don't need an 'else' unless we use an if or elif statement within the loop
#assign multiple variables on one line
# username, password, day_of_week, = 'hello', 'how', 'are you'
# print(username)
# print(password)
# print(day_of_week)

# initialize multiple variables on one line
# username, password, day_of_week, = '', '', ''


'''
Exercise

Improve the login system we wrote last class to allow multiple attempts. You're developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.


'''

#Set sys id and pass
# sys_id = 'admin'
# sys_password = 'password'

# # Prompt User - for people that get it right the first time, they will not enter the loop
# user_id = input('Please enter your username: ')
# user_password = input('Please enter your password:')

# # Our initial check, while not equal we will enter loop
# while sys_id != user_id and sys_password != user_password:
#     # we have entered the loop, this means the username and password did not match.
#     print('Incorrect username and password')
#     user_id = input('Please enter your username: ')
#     user_password = input('Please enter your password:')

# print('Login Sucessful!') #this is outside of the loop because it is left aligned



# ''' For Loops '''




# STRING
my_string = 'Supercalifragilisticexpialidocious'
# for s in my_string:
#     print(s) #prints each letter in string

# LIST
my_list = ['dog', 'cat', 'bird', 'giraffe', 'fox', 'elephant', 'mouse', 'zebra']
# for animal in my_list:
#     print(animals) #prints each item in list

# TUPLE
my_tuple = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
# for months in my_tuple:
#     print(months)

'''Dictionary works a bit different, 
they have key value pairs'''
# DICTIONARY
my_dictionary = {"First name": "Jill",
                 "Last name": "Simmons",
                 "Age": 34,
                 "Address":"1515 Mockingbird Lane"}

# for keys you need to use the keys method
# for k in my_dictionary.keys():
    # print(k)

#for values you need to use the value method
# for v in my_dictionary.values():
    # print(v)

#for key value pairs
# for k, v in my_dictionary.items():
#     print(k, v)

# SET
my_set = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# for days in my_set:
#     print(days)


# RANGE
# for x in range(10,25):
#     print(x)


'''
TRICKY
Write a for loop that print how long the string is.
'''
# my_string = 'Supercalifragilisticexpialidocious'
# total = 0 #initialize for final count

# for m in my_string:
#     total += 1
# print(f'There are {total} letters in your word, {my_string}.')


''' Exercise

Take a string from the user. Verify that it's a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop
'''

# user_input = input('Please enter your number:')
total = 0 #initialize

#we will use our conditionals in the for loop
# for t in (user_input):
#     if user_input.isdecimal(): # once we confirm this is a number
#         t = int(t) #cast to an integer
#         total += t #every time through, we will add that value to sum
# print(f'Your total is {total}')

#check what happens when print() is tabbed in 



''' Exercise 
Write some code that will loop through a string and print whether each letter is a vowel or consonant.

Example:
'hello'
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel


'''

'''VERSION ONE'''
# word = 'hello'
# vowels = ['a', 'e', 'i', 'o', 'u']

# # for w in word:
# #     if w in vowels:
# #         print(f'{w} is a vowel')
# #     else:
# #         print(f'{w} is a consonant')

'''VERSION TWO'''
# word = input('Please insert your word: ')
# vowels = 'aeiou'

# for w in word:
#     if w in vowels:
#         print(f'{w} is a vowel')
#     else:
#         print(f'{w} is a consonant')

'''VERSION THREE'''

# word = input('Please input your word:')

# for w in word:
#     if w in 'aeiou':
#         print(f'{w} is a vowel')
#     else:
#         print(f'{w} is a consonant')

''' Exercise 
You're working on a data analysis project for a company that looks at written text. You're only interested in letters from A-Z because you're analyzing language. However, the data you're given has some values that shouldn't be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn't a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''

'''For loop with a conditional'''
# result = '' #initialize
# user_input = input('Please enter your data:')

# for u in user_input:
#     if u.isalpha():
#         result += u
#     else:
#         print(f'Sorry {u} is not a letter')
# print(result)



    








