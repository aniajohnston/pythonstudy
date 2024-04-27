import math
import class19.assignment.name_module as name_module

# print(name_module.full_name(firstname, lastname))
# print(name_module.reverse_name(firstname, lastname))
# print(name_module.get_initials(firstname, lastname))
# name_module.full_name('Joe', 'Smith')

'''Regular Function'''
# def hello_world():
#     print('hello world')

# hello_world() #function call

'''Function with a print statement'''
# def greeting(name):
#     print("Hello", name)

# greeting('Sarah') #function call, argument is Sarah

'''Function with a return statement'''
# def greeting(name):
#     return f"Hello {name}"

# print(greeting('Sarah')) # To see a returned value, put entire function call within the print statement

'''Function with return statement and a variable'''
# def greeting(name):
#     return f'Hello {name}'

#assign function call to a varaible
# my_name = greeting('Dana')
# print(my_name)

'''Modify a parameter'''
# def double_me(value):
#      result = value * 2
#      print(result)

#Function call with variable
# num = 10
# double_me(num)

#Function call with parameter
# double_me(100)

'''Modify a parameter pt. 2'''
# def double_me(value):
#     return value * 2

# result = double_me(100) #assign function call to result
# print(result)

'''Modify a parameter pt. 3'''
'''BEST METHOD'''
# def double_me(value):
#     result = value * 2
#     print(f'{value} doubled is {result}.')

# double_me(100)



'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''

'''ALL ON ONE PAGE'''
# def vowel_or_not(word):
#        vowels = 'aeiou'
#        for w in word:
#           if w in vowels:
#                print(f'{w} is a vowel')
#           else:
#                print(f'{w} is not a vowel')
# my_word = 'Hollywood'
# vowel_or_not(my_word)


'''USING A SEPERATE PAGE'''
'''1. Copy the above definition and put it onto the document name_module.py'''

'''import name_module'''

'''3. Call name_module and use the method value_or_not with the parameter or your choosing'''
# name_module.vowel_or_not('America')

'''
Example

Write a function that returns the surface area of a box (rectangular prism).
Surface Area = 2 * ((width*length + (length*height) + (height*width))

'''

'''OPTION 1'''
# #write the function
# def surface_area(width, length, height):
#     return 2 * ((width*length) + (height*length) + (height* width))

# #FIRST METHOD print entire function call
# print(surface_area(5, 3, 6))
# #SECOND METHOD send the function call to a variable
# total = surface_area(5, 3, 6)
# print(total)

"""OPTION 2"""
# width = 5
# length = 3
# height = 4

# def surface_area(w, l, h):
#     return 2 * ((w*l)+(l*h)+(h*w))

# print(surface_area(width, length, height))



'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2
'''

'''MY SOLUTION'''
# radius = 2

# def surface_area_sphere(r):
#     return float(4) * 3.14159 * float(r** 2)

# print(surface_area_sphere(radius))

"""DANIEL'S SOLUTION"""

# radius = 6.0 #write your radius as a float

# def surface_of_sphere(r):
#     return 4 * math.pi * radius **2

# print(surface_of_sphere(radius))



''' Lets follow these functions through line by line and analyse the return statements'''
# def get_vowels(word):
#     out = '' #empty string
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w #appending vowel to empty string
#     return out

# my_word = 'bananas'

# '''function call by itself won't print'''
# get_vowels(my_word)
# '''function call with the print statement will print out the return'''
# print(get_vowels(my_word))

'''PRINT VOWELS'''
# Return is none
# def print_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
#     print(out)

# my_word = 'bananas'

# print_vowels(my_word) #prints the results of line 101
# print(print_vowels(my_word)) # this is the 'return' format and this will result in the word "None" to be printed in the terminal since we are not using 'return'



'''
Exercise
1. Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
2. Return how many times the value was removed.
'''

# sample_list = [4,5,3,2,4,3,3,3,3,2,2,1,1,1,1,0,5]
# value = 5

# def val_count(my_list, my_value):
#     counter = 0
#     while my_value in my_list:
#         my_list.remove(my_value)
#         counter += 1
#     return counter



# result = val_count(sample_list, value)
# print(f'{value} appears {result} times.')

'''
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:
transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}

'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},\
                {'id': 'c', 'amount': 545, 'type': 'deposit'},\
                {'id': 'c', 'amount': 225, 'type': 'withdrawal'},\
                {'id': 'b', 'amount': 45, 'type': 'withdrawal'},\
                {'id': 'e', 'amount': 150, 'type': 'deposit'}]

'''Write our function'''
# def transaction_logs(transaction_data):
#     output = {}
#     for t in transaction_data:
#         #if ID doesn't yet exist, add it to our output dictionary
#         if t['id'] not in output.keys():
#             if t['type'] == 'deposit': #checking for deposits
#                output[t['id']] = t['amount'] #add deposits amount to ID key
#             else:
#                 #otherwise it exists, let's check to see if it's a withdrawl or deposit
#                 if t['type'] == 'withdrawal':#checking deposit
#                     output[t['id']] -= t['amount']
#                 else:
#                     output[t['id']] += t['amount']
#     return output


'''Output our function'''
# print(transaction_logs(transactions)) #our function call, with our list of dictionaries


''' Create a python file called name_module.py. Inside this python file, you will create 3 functions. One called full_name, another called reverse_name, and a third called get_initials. Each function will take 2 strings. One string will be the first name, the second string will be the last name. full_name will concatenate and return the full name. For example if the first string is "Joseph" and the second string is "Simpson" This function will return the string, "Joseph Simpson". Reverse name will flip the name around. The name Diana Prince, would come back as Prince Diana. The third function will take the first and last name and return the initials. The name Tony Stark will return T.S. Now create a second python file, called name.py. Import the module you just created and call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal'''

