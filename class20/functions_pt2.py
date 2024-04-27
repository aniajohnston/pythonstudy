import statistics

# Functions Part 2

# With documentation and type hinting (optional)

# def my_function(country: str = 'Norway') -> None : #country: str is called 'type hinting' The arrow means we are not returning anything
#     '''I am explaining what my country does

#     -country parameter with default value
#     '''
#     print("I am from", country)

# my_function("Sweden") #overrides
# my_function("Brazil") #overrides
# my_function() #uses default



'''
Exercise
Write a function called center that returns either the mean or median of a list of numbers.
This function should take two parameters: A list of numbers, and an optional parameter called use_median which should default to False.
If use_median is False, return the mean of the list.
If use_median is True, return the median of the list.
Test your function by calling it with different arguments.
'''

'''No documentation or type hinting'''


# def center(my_list, use_median=False): #use median defaults to False
#     if use_median == False:
#         return statistics.mean(my_list)
#     else:
#         return statistics.median(my_list)


# test_list1 = [1,2,2,2,3,4,5,6,7,8]
# test_list2 = [3,6,7,9,10,11,2]

# my_median = center(test_list1, True)
# my_mean = center(test_list1)
# my_mean_two = center(test_list1, False)
# print(my_median)
# print(my_mean)
# print(my_mean_two)



# '''Documentation, type hinting, shorthand if-then-else'''

# def center(my_list:list, use_median: bool = False) -> float: #with type hinting
#     '''Return either mean or median of a list of numbers
    
#     -my_list: the list to extract mean or median
#     -use_median: bool to select mean or median
#     '''
#     return statistics.mean(my_list) if use_median == False else statistics.median(my_list)

# test_list1 = [1,2,2,2,3,4,5,6,7,8]
# test_list2 = [3,6,7,9,10,11,2]

# my_median = center(test_list1, True)
# my_mean = center(test_list1)
# my_mean_two = center(test_list1, False)
# print(my_median)
# print(my_mean)
# print(my_mean_two)




# Returning multiple values

# def get_vowels_and_consonants(word):
#     vowels = ''
#     consonants = ''
#     for letter in word:
#         if letter in 'aeiou':
#             vowels += letter
#         elif letter in 'bcdfghjklmnpqrstvwxyz':
#             consonants += letter
#     return vowels, consonants

# vowels, consonants = get_vowels_and_consonants("apple")

# print(vowels)
# print(consonants)


'''
Exercise
Write a Python function called get_stats that takes in a list of numbers and returns the following three values: The mean, the median, and the mode of the list.
Call the function on a list, and print each statistic on a separate line.
my_list = [1,2,4,5,5]
Output:
Mean: 3.4
Median: 4
Mode: 5
'''

my_list = [1,2,4,5,5]

# def get_stats(list):
#     return f'Mean: {statistics.mean(list)}\nMedian: {statistics.median(list)}\nMode: {statistics.mode(list)}'

# print(get_stats(my_list))




'''Global variables'''

# x = 'challenging'
# def change_x():
#     x = 'fun'

# change_x()
# print("Programming is", x)


# x = 'challenging'
# def change_x():
#     global x
#     x = 'fun'
    
# change_x()
# print("Programming is", x)

'''
A lambda is a small anonymous function. It can take any number of arguments, but it can only have one expression, which is returned.
Syntax: lambda arguments : expression
'''

# Function to add two numbers



# Written as a Lambda




# Write the following functions as Lambdas

def greeting(fname):
    print(f'Hello, {fname}')


def double_me(num):
    return num + num


'''
Exercise
Write a lambda that computes the n-th power of a number, given two arguments, num and n.
Now, write a function that is equivalent to the lambda.
'''





''' Higher Order Functions
These are functions that may accept a function as an argument or return a function as its output. In Python, reduce(), map() and filter() are some of the most important higher-order functions. When combined with simpler functions, they can be used to execute complex operations.

filter - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

map - returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''
# Let's use the filter function to find the even numbers in a list



my_list = [0,1,2,3,4,5,6,7,8,9,10]

# Triple Me! Triple the numbers in this lsit

triple_me = [0,1,2,3,4,5,6]

# Lambda with sort

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]



'''
Assignment 6
Write a simple function that returns a person's net worth. Here are your requirements:
Docstring which includes what function does and information on your parameters (brief)
Function name - net_worth
parameters - assets, liabilities
Must contain type hinting for the parameters as well as what the function will be returning
Call the function in a print statement with needed arguments
'''




