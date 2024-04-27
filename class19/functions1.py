import math
import name_module

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
Surface Area = width*2 + length*2 + height*2

'''


'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2

'''



''' Lets follow these functions through line by line and analyse the return statements'''

# def get_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     return out

# my_word = 'bananas'

# get_vowels(my_word)
# print(get_vowels(my_word))

# Return is none
# def get_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     print(out)

# my_word = 'bananas'

# get_vowels(my_word)
# print(get_vowels(my_word)) # Return None



'''
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''

sample_list = [4,5,3,2,4,3,3,3,3,2,2,1,1,1,1,0,5]
value = 5



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




''' Create a python file called name_module.py. Inside this python file, you will create 3 functions. One called full_name, another called reverse_name, and a third called get_initials. Each function will take 2 strings. One string will be the first name, the second string will be the last name. full_name will concatenate and return the full name. For example if the first string is "Joseph" and the second string is "Simpson" This function will return the string, "Joseph Simpson". Reverse name will flip the name around. The name Diana Prince, would come back as Prince Diana. The third function will take the first and last name and return the initials. The name Tony Stark will return T.S. Now create a second python file, called name.py. Import the module you just created and call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal'''

