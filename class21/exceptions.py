import math



''' Compile time errors / static errors'''
# SyntaxError: unterminated string literal


# SyntaxError: '(' was never closed

# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# SyntaxError: expected ':'


''' Exceptions / Runtime errors'''

''' ValueError '''
# ValueError: could not convert string to float: 'testing'

# ValueError: math domain error

# ValueError: not enough values to unpack (expected 3, got 2)

''' AttributeError '''

# AttributeError: 'int' object has no attribute 'append'
num = 10

# AttributeError: 'str' object has no attribute 'append'
str1 = 'hello'

''' NameError '''
# NameError: name 'x' is not defined

#name 'c' is not defined

''' TypeError '''
#TypeError: can only concatenate str (not "int") to str


# TypeError: 'str' object is not callable

# TypeError: list indices must be integers or slices, not str


# TypeError: 'int' object is not iterable


# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Keyboard interruption exception

# KeyboardInterrupt



# Lets prevent a user from dividing by zero




# Lets implement a try, except, to prevent a user entering a regular word







'''
Exercise - Handling Invalid User Input
Write a Python program that takes a customer's age as user input and determines whether they're eligible for a senior discount.
Sometimes the age might not be in the correct format. Handle this using try-except, and print a descriptive error message if the age can't be cast to an int.
If the age is greater than or equal to 65, the customer is eligible for the discount. Otherwise, they're not eligible. Print whether the customer is eligible or not.

'''




# With Except



# With Except / Else

# With Except / Else / Finally


''' Exercise 

You can add a finally block that will be executed regardless if the try block raises an error. 
This is good for cleaning up resources, because it will always be run.

Let's create a function out of the following code

# userin = input("Enter a number: ")
# num_list = []
# try:
#     num_list.append(float(userin))
#     print(num_list)
# except ValueError:
#     print("Number value only please.")

'''





''' Exercise - Raising exceptions
Write a program to take the square root of user input.
Use a try-except statement to ensure the user inputs a float.
If the user inputs a negative number, raise a ValueError that will also be caught by the except statement. Make sure to write a descriptive message in the exception you raise.
'''



# Propogating exceptions (functions)

# Function that calculates average of two numbers






'''
Exercise

You have been assigned the task of creating a sales tax calculator for an e-commerce company. Write a Python function called calculate_final_price that takes the price of a product and the sales tax rate, and return the final price including tax.
The price should be a positive number, and the tax rate should be between 0 and 1 (exclusive). If either of them are outside of the valid range, raise a custom ValueError with an appropriate error message.
Now, test your implementation by asking the user to input a product price and sales tax rate, and call your function. Catch any potential ValueError raised by the function.
'''



    








