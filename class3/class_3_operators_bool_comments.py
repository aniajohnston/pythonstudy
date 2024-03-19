# Operators, Boolean Expressions, and Comments

# I am a comment

# Everything after the hash will be ignored when you run your code

temperature = 95 # I can be an inline comment

# Or I can be a standard single-line comment
weekday = 'Wednesday'


first_name = 'Thomas' ''' Multi-line comments can be inline '''
last_name = 'The Train' """ Holding shift and clicking double quotes three times makes an inline comment as well """


'''
Will be a multi line comment

'''

'''This will be inline'''

"""This behaves the same"""

'''
I am a multi-line comment and 
can easily be used to span 
multiple lines in a Python file
'''

"""
You can also use the double quotes
to create as a multi-line comment.
Anything in between these three quotes will not run
"""

'''
Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!
'''

'''
Ensure that your comments are clear and easily understandable to other speakers of the language you are writing in.

'''

'''
An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
'''

# Inline comments are unnecessary and in fact distracting if they state the obvious.

# Comment me!

#we are solving for the perimeter of a rectangle

# length = 5  #this is the length of our rectangle
# width = 7  #this is the width of our rectangle
# # Perimeter of my rectangle
# perimeter = 2 * (length + width)
# # print(perimeter) #here we printed the answer


# # Comment me!
# # Tuesday's temperature
# fahrenheight = 89 
# # Convert farenheight to celcius
# celsius = (fahrenheight - 32) * 5/9
# # print(celsius) #here we test


'''Shortcut operators'''

# Add 5 to me using shortcut operator +
# age = 25
# age += 5
# print(age)


# Add 10 to me using shortcut operator +
# year = 2024
# year += 10
# print(year)


# Subtract 20 -
# num_one = 55
# num_one -= 20
# print(num_one)


# Subtract 15 -
# num_two = 11
# num_two -= 15
# print(num_two)


# Multiply by 3 *
# my_value = 9
# my_value *= 3
# print(my_value)



# Multiply by 10 *
# mileage = 15
# mileage *= 10
# print(mileage)


# Divide by 2 /
# pizza_slices = 8
# pizza_slices /= 2
# print(pizza_slices) 


'''Does division always return a float?

YES'''

#Divide by 7 /
# fees = 8.90
# fees /= 7
# print(fees)

# Raise to the 3rd power **
# num_three = 6
# num_three **= 3
# print(num_three)




# Raise to the 2nd power **
# data = 16
# data **= 2
# print(data)

'''With Integer Division:
Think: how many times does the divide by
fit into the variable value'''


# # Integer divide by 3 //
# val_one = 16
# val_one //=3
# print(val_one)
'''Does not return a remainder with the answer'''


# Integer divide by 4 //
# val_two = 9
# val_two //= 4
# print(val_two)

'''Mod returns the remainder'''

# # Find the remainder if divided by 3 %
# val_three = 10
# val_three %= 3
# print(val_three)




# # Find the remainder if divided by 5 %
# val_four = 14
# val_four %= 5
# print(val_four)


# Refactor the fahrenheit/celsius converter using shortcut operators

'''without shortcut operators'''
# farenheit = 89 
# celsius = (farenheit - 32) * 5/9
# print(celsius)
# '''with shortcut operators'''
# farenheit = 89
# farenheit -= 32
# farenheit *= 5/9
# '''think about this as casting a 
# variable to another variable'''
# celcius = farenheit 
# print(celcius)

''' Boolean Operators'''

# Is 7 less than 5? <
# print(7 < 5)

'''why do we asign to result?
for readability'''


# result = (7 < 5)
# print(result)

# Is 4 less than or equal to 4? <=
# print(4 <= 4)
# result = (4 <= 4) 
# print(result)

# # Is 6 greater than 2? >
# result = (6 > 2)
# print(6 > 2)

# Is 5 greater than or equal to 6? >=
# result = (5 >= 6)
# print(result)

# Is 5 equal to 5? ==
# print(5 == 5)
# result = (5 == 5)
# print(result)

# Is 100 not equal to 75? !=
# print(100 != 75)
# print(100 != 100)
# result = (100 != 75)
# print(result)

# and
'''and applies boolean to however 
many results are run together'''
#this is true because both are true
# print(2==2 and 3 == 2) #this is false because one is false
# print(1==0 and 3==5) #this is false because both are false

'''You can use and to link variables together
and check for Boolean'''
# logic_1 = (5 == 5)
# logic_2 = (4 == 4)
# print(logic_1 and logic_2)


'''Or will give you true if one or the other is true
if at least 1 are true'''
# or
# print( 100==100 or 45>70)


'''Not gives us the opposite'''
# not
x = 5
y = 7

# is x < y?
# print(x < y)
# print(not x < y)

'''REVIEW'''
# Are we the same object? is 
# fname = 'Taylor'
# new_name = fname
# print(fname is new_name)


'''in '''
# print('J' in 'January')
# print('F' in 'March')

# eval

# is_open = 'True'
# weekday = 'False'
# print(eval(is_open))

