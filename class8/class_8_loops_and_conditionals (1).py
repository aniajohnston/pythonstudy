''' Loops and conditionals '''

'''
What is the difference between a For and While Loop?
How do I write a For Loop?
How do I write a While Loop?

'''




# For Loop
# colors = ['green', 'blue', 'orange', 'yellow'] #you can solve the taken usernames problem

# for c in colors: 
#     print(c)

# While Loop

# limit = 26 #initialization of variables
# start = 0 #it doesn't matter

# while start < limit: #condition
#     print(start) #feedback for the user
#     start += 1

''' Break Keyword '''

#initializing on one line
# south, north, west, east = '', '', '', ''

# Lets look at the 2 examples below and take note where the loop stops


'''Example 1: Breaking out with stop'''
userin = '' # initialization of variable

# while userin != 'stop':
#     userin = input("Enter something or hit stop to leave the loop")
#     print(userin)

# while True:
#     userin = input("Enter something or hit stop to leave the loop ")
#     if userin == 'stop':
#         break
#     print(userin)


''' Break in nested loops '''
'''test one'''
# i = 3
# while i > 0:
#     print(i)
#     i -= 1
#     if i == 4:
#         break
# else:
#     print('done')
'''test two'''
# i = 6
# while i > 0:
#     print(i)
#     i -= 1
#     if i == 4:
#         break
# else:
#     print('done') #does not print done because it breaks when it gets to four

'''Next exercise'''
# userin = '' 
# #taking a string from the user until they hit stop
# while userin != 'stop':
#     userin = input("Please enter a word or hit stop to end the loop ")

#     for l in userin: #looping through the input from the user
#         if l.isalpha(): #testing to see if each character is in the alphabet
#             print(l)
#         else: 
#             break # break only breaks out of the for loop
#     print("This is our next line of the for loop") # still inside for loop goes back to 74 after
    
# print("This will print when loop is complete") #only prints when the loop is stopped
# #for example, if we type in number, it will go back to userin = input() line

'''BEST EXAMPLE - 'break' in nested loops'''
# for i in range(3):   # Outer loop
#     for j in range(2):   # Inner loop
#         if j == 1:
#             break   # Exit the inner loop when j equals 1
#         print(i, j)


'''next excercise'''    

# while True:
#     userinput = input('Please enter your word')
#     print('We are on line 84')
#     print(userinput)
#     print("we are still in the while loop")
#     break
#     print('I do not get printed')
# print('Why do I get printed?') #this is outside the loop

'''
Exercise

Write some code that takes in numbers from a user one at a time. This should keep going until the user enters 0. Then print the sum of all the numbers.
If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):
5
7
c
Error: Not a number

'''




'''MY ATTEMPT'''
# userin = ''
# total = ''

# while True:
#     userin = input('Please enter a number: ')

#     for u in userin:
#         if u.isdigit():
#             print(u)
#             total += u
#             print(total)
#         else:
#             break


"""Prof attempt"""

'''Declare any needed variables'''

# user_input = ''
# total_sum = 0

'''Start our loop'''
# while True:
#     user_input = input('Please enter your number: ')
#     '''Test for letter'''
#     if user_input.isalpha():
#             print('This is false.')
#             break
#     '''Convert to integer, end and print sum if zero, otherwise continue to add to sum'''
#     user_input = int(user_input) #recast to integer
#     '''When the user types 0, the program does the final calculation'''
#     if user_input == 0:
#         print(f'Sum: {total_sum}')
#         break
#     else:     
#         total_sum += user_input


''' Continue keyword '''


     
''' Example
Use the continue keyword to loop through a string and only print the vowels.
'''
# Option 1
test_string = 'hello'
# vowels = 'aeiou'
# vowels = ['a','e','i','o','u'] #use this for taken usernames

# for t in test_string:
#     if t in vowels:
#         print(t)
#     else:
#         continue

# Option 2
# for t in 'aeiou': #shortens the code
#     if t in vowels:
#         print(t)
#     else:
#         continue


''' 
Exercise:
Sum of Even Digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''

'''MY VERSION'''
# user_input = input('Please enter your number: ')
# user_sum = 0

# for u in user_input:
#      user_input = int(user_input)
#      if user_input % 2 != 0:
#         continue
#      else:
#          user_sum += user_input
#          print(f'Your total is: {user_sum}')

'''Professor's version'''
# user_input, sum = '', 0

# while True:
#     user_input = input('Please enter your string: ')
#     for u in user_input: #loop through the string entered by the user
#         if u.isalpha():
#             continue
#         else:
#             u = int(u) #recasting to a number
#             if u % 2 == 0:
#                 sum += u
#     print(sum) #line this up with for

''' Break, Continue, and Pass '''
# word = 'hello'
# vowels = 'aeiou'

# for l in word:
#     if l in vowels:
#         print(l)
#         break #broke after first vowel in word.

# for l in word:
#     if l in vowels:
#         continue
#     print(l)

# for l in word:
#     if l in vowels:
#         pass #lets you skip the if condition
#     print(l)

'''
Exercise

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.

'''


'''These variables will be placeholders for the total and new string we will be creating'''
new_total = 0
new_string = ''

# while True:
#     user_input = input("Please enter your data: ")

#     #if empty stop the loop
#     if len(user_input) == 0:
#         print('String is empty, stopping the loop')
#         break
#     #if the string is a number convert to a float and add it to a total
#     elif user_input.isnumeric():
#         user_input = float(user_input)
#         new_total += user_input
#         print(f'Updated total to {new_total}')
#         continue #VERY IMPORTANT, NEEDS TO BE HERE
#     #concatenate to new string
#     elif user_input.isalpha():
#         new_string += user_input
#         print(f'Your updated string is {new_string}')
#         continue
#     #check for special characters
#     elif not user_input.isalnum():
#         print(f'{user_input} is a special character, no action and lets continue')
#         continue

'''Error messages'''
error_messages = ['Username taken', 'Password taken', 'Error message 3'] #you can index this for error messages
#to reference error messages: print(error_messages[0])