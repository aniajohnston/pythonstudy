''' Variables and Operators '''
# Create a variable for your first name and a variable for your last name. Concatenate and print them in a new variable called 'fullname'.

# Create a variable called greeting and assign it to string value of 'hip hop hooray'. Using multiplication, create a third variable called 'three cheers' which repeats greeting 3 times.


''' Arithmetic Operators  '''

# add 100 to 50

# add 25 to 60

# multiply 5 and 5

# multiply 6 and 3

# subtract 15 from 45

# subtract 60 from 100

# raise 5 to the 2nd power

# raise 6 to the 3rd power

# raise 4 to the 8th power

# 10 divided by 5

# 7 divided by 3

# 10 divided by 3, drop the remainder

# 9 divided by 5, drop the remainder

# Remainder of 14 divided by 5

# Remainder of 12 divided by 8

''' Comparison Operators '''

# Is 5 greater than 7?

# Is 10 less than 4?

# Is 8 less than or equal to 14?

# Is 10 less than or equal to 10?

# Is 6 equal to 7?

# is 100 equal to 100?

# Is 15 not equal to 11?



''' Strings '''

# Check if the following string is lowercase, use meaningful variable names

day = 'tuesday'

check_lowercase = day.islower()
# print(check_lowercase)

# Check if all the characters in the text are in upper case:
# The isupper() method returns True if all the characters are in upper case, otherwise False.

word = 'WEDNESDAY'
check_uppercase = word.isupper()
# print(check_uppercase)

''' The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.'''

# Use the isidentifier method on the following username variables

username = '#$(@#@#$#@)'
username_id = username.isidentifier()
# print(username_id)

username2 = 'simonsays_90'
username_id = username2.isidentifier()
# print(username_id)

username3 = '3492_sdfsdf' #false because it starts with a number
username_id = username3.isidentifier()
# print(username_id)


username4 = 'hello*world'
username_id = username4.isidentifier() #contains a special character
# print(username_id)





# convert to lowercase

make_me_lower_case = 'HALLOWEEN'
lower = make_me_lower_case.lower()
# print(lower)

# convert to uppercase
make_me_upper_case = 'valentines day'
upper = make_me_upper_case.upper()
# print(upper)

# Is this proper title case?
string = "the eye of the tiger"
title = string.istitle()
# print(title)

# Put all list items in a string
# join
my_list = ['jean', 'sarah', 'larry']
my_string = ' '.join(my_list)
# print(my_string)


# Replace J with B
test_name = 'jerry'
replace = test_name.replace('j','B')
# print(replace)


# split this string and place each word in a list
string = 'I would like to split up this string'
new_string = string.split()
# print(new_string)
# print(type(new_string))


# Check if this string starts with a letter w
str = 'zootopia'
result = str.startswith('w')
# print(result)



''' Conditionals - if/else statements '''

# Check if num 1 is greater than num 2. Print the results to the user and use a formatted string

num_1 = 10
num_2 = 9

# if num_1 > num_2:
#     print(f'{num_1} is greater than {num_2}.')
# else:
#     print(f'{num_1} is not greater than {num_2}.')





''' Loops - For/While'''

# Write a while loop that will count from 0 to 50


#option one
# start = 0
# stop = 51
# while start < stop:
#     print(start)
#     start += 1

#option two
# start = 0 #think of start as our counter variable
# end = 50

# while start <= end:
#     print(start)
#     start += 1


# Write a while loop that will count down from 65 to 25
# start = 65
# stop = 25

# while start >= stop:
#     print(start)
#     start -= 1


# Write a while loop that will ask start at 100 and count down to 50, however, put some logic into the loop so the loop stops at 75
 
start = 100
stop = 50

#option 1

# while start >= stop:
#     print(start)
#     start -= 1
#     if start == 74:
#         break

#option 2 (more fancy)

# while start >= stop:
#     print(start)
#     start -= 1
#     if start == 75:
#         print(f'Your ending value is {start}.')
#         break




# Write a for loop that will loop through the string below and copy/move these letters to the new empty string'''

str_1 = 'Have a happy birthday'
str_2 = ''

# for s in str_1:
#     if str_1 not in str_2:
#         str_2 += s #adds every character from string 1 to string 2
# print(str_2)


    
''' Loops & Conditionals'''
# write a for loop to loop through this list and tell the user if the number is even or odd
    
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for n in num_list:
#     if n % 2 == 0:
#         print(f'{n} is even.')
#     else:
#         print(f'{n} is odd.')







# write a for loop to loop through this string and tell the user if the number is vowel or a consonant

vowels = 'aeiou'
my_string = 'abracadabra'

# for m in my_string:
#     if m in vowels:
#         print(f'{m} is a vowel.')
#     else:
#         print(f'{m} is not a vowel.')



# In a while loop, ask the user for their favorite animal. If the word is equal to giraffe, we will tell the user congratulations and end the loop. Otherwise we will keep prompting the user.

user_input = ''

keyword = 'giraffe'

# while True:
#     user_input = input('Please guess the animal: ')
#     user_input.strip()
#     if user_input == keyword:
#         print('Congrats, you guessed it!')
#         break
#     else:
#         print(f'Sorry, try again. {user_input} is not the correct guess.')





# In a while loop, ask the user for a word in all lowercase. If the string is not all lowercase, reprompt the user until the condition is met

# HINT The isupper() method returns True if all the characters are in upper case, otherwise False.

user_input = ''

# while True:
#     user_input = input('Please enter a lowercase word: ')
#     if user_input != user_input.isupper():
#         print(f'{user_input} is a lowercase word.')
#         break
#     else:
#         print(f'Sorry, {user_input} is not a lowercase word.')
#         continue




        
# Create a while loop, We will ask the user for a string, the first character of the string must be a number, the last character must be a capital letter to pass testing. Otherwise the user must keep trying.

test_word = '1helloH'
user_input = ''

# while True:
#     user_input = input('Please enter a string where the first character is a number and the last is a capital letter: ')
#     if user_input[0].isnumeric() and user_input[-1].isupper():
#         print(f'You have passed the tests!')
#         break
#     else:
#         continue
    





        
    


''' Lists '''

# Loop through the full list, and copy all the items in that list into the empty list
full_list = ['Move', 'me', 'to', 'an', 'empty', 'list', 'with', 'append']
empty_list = []

# for n in full_list:
#     if n not in empty_list:
#         empty_list.append(n)
# print(empty_list)
        




# Lets practice some more indexing

my_super_list = [['superman', 'wonderwoman','batman'],['spiderman','captain america','ironman'],['aquaman']]

# Create a variable and assign it to wonderwoman via indexing
# wonderwoman = my_super_list[0][1]
# print(wonderwoman)

# Create a variable and assign it to spiderman via indexing
# spiderman = my_super_list[1][0]
# print(spiderman)

# Create a variable and assign it to aquaman via indexing
# aquaman = my_super_list[2][0]
# print(aquaman)