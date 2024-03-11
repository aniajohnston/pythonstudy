''' Class 4 Strings '''

# String operators

'''Concatenation - for readability'''
operator_code = 'A987'
part_id = '49Be'
# print(operator_code + part_id) #we want to get into the habit of putting this into a variable
item_number = operator_code + part_id
# print(item_number)

''' Create two variables, one to capture first name, another for last name. Combine them to a third variable to display the user's full name. '''
first_name ='Ania'
last_name = 'Johnston'
full_name = first_name + ' ' + last_name
# print(full_name)

''' Multiplication '''
greeting ='hip hip horray ' * 3
# print(greeting)

''' Using multiplication, create a new string that multiplies your favorite color 5 times'''
color = 'blue ' * 5
# print(color)



# Reference vs Value equality (== vs. is)
x = 'hello'
str2 = 'HELLO'.lower() #dot lower string method is being applied to this string

# print(x)
# print(str2)

# print(x == str2) #true
# print(x is str2) #false, two different variables

# #we can use id() to check whether these objects are the same or not
# print(id(x))
# print(id(str2)) #these two objects are not the same



''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''
test_character = 'b'
test_string = 'bananas'
# is test_character in test_string
# print(test_character in test_string)

''' create a quick test to see if the sub string 'spreh' can be found in the string 'Incomprehensibilities' '''
test_chars = 'spreh'
test_word = 'Incomprehensibilities'
# print(test_chars in test_word)




''' len() - function - Returns the length of a string, aka the number of characters in a string.'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
length_of_alphabet = len(alphabet) 
#what parameters are needed for len? 
# alphabet is the argument
# len has a parameter and it's accepting that object 
# print(length_of_alphabet)

''' create a variable that holds a string of your favorite animal, create a variable to capture the length of that animal's string value'''
animal = 'zebra'
length_of_animal = len(animal)
# print(length_of_animal)



# String methods

word_1 = 'happy' # capitalize me! capitalizes first letter
# print(word_1.capitalize()) #parameter is being applied, DONT FORGET ()
# print('happy'.capitalize()) #here we are applying it directly to the string

ex_1 = 'cereal' # capitalize me!
# print(ex_1.capitalize())

word_2 = 'SuPrISe' # make me lower case! #casefold()
# print(word_2.casefold())

ex_2 = 'RuMMaGe' # make me lower case! #lower()
# print(ex_2.lower())
# print(ex_2.casefold())

word_3 = 'ZOO' # make me lower case!
# print(word_3.casefold())
# print(word_3.lower())

ex_3 = 'PLANET' # make me lower case!
# print(ex_3.casefold())
# print(ex_3.lower())


'''FUN FACT: Whereas casefold() method is an advanced version of lower() method, it converts the uppercase letter to lowercase including some special characters which are not specified in the ASCII table for example ‘ß’ which is a German letter and its lowercase letter is 'ss'.
'''

word_4 = 'Good Evening'
# print(word_4)
#the center() method needs a parameter, let's test it out!
# print(word_4.center(100)) #takes up 100 characters and centers the string
# print(word_4.center(50)) #takes up 50 characters and centers the string

ex_4 = 'Hello World!' # center me within a space of 65 characters
# print(ex_4.center(65)) #takes up 65 characters and centers the string
# print(ex_4.center(3)) #takes up 3 characters and 'centers' the string




word_5 = 'Pseudopseudohypoparathyroidism' # How many p's? use the count method that takes a parameter
'''There are actually 4 p's but the count() method is case sensitive, use lower()/casefold() to make the input lowercase before using the count() method'''
# print(word_5.count('p'))

ex_5 = 'Antidisestablishmentarianism' # how many times does the letter 'e' occur?
# print(ex_5.count('e'))


'''ESCAPE CHARACTERS'''

"""Expand Tabs - needs an argument + has a parameter"""
word_6 ='I\tam\ta\ttab'# expand tabs
# print(word_6)
# print(word_6.expandtabs(10)) #expands all tabs by declared white spaces

create_new_line = 'I\n am\n a\n new\n line\n'
# print(create_new_line)

ex_6 = "Let's\t do\t some\t coding!" # lets try to increase the tabs to 10 whitespaces
# print(ex_6)
# print(ex_6.expandtabs(10))


# Find the position of the letter k
word_7 = 'Omphaloskepsis'
# print(word_7.find('k')) #begins at zero position

ex_7 = 'Dichlorodifluoromethane' # find the position of the letter f
# print(ex_7.index('f'))

word_8 = 'Supercalifragilisticexpialidocious'
# print(word_8.find('g')) # needs a parameter #argument is 'g' #gives us 12 and counts 0
# print(word_8.index('g'))

'''Fun Fact - Both index() and find() are identical in that they return the index position of the first occurrence of the substring from the main string. The main difference is that Python find() produces -1 as output if it is unable to find the substring, whereas index() throws a ValueError exception.'''


# isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z and 0-9

test_1 = 'abcdef'
test_2 = '%$123' #not a-z or 0-9

# print(test_1.isalnum())
# print(test_2.isalnum())

ex_8 = '123*' # Am I alphanumeric?
# print(ex_8.isalnum())


# isalpha() Are all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345' #is not in the alphabet
# print(test_3.isalpha())
# print(test_4.isalpha()) 

ex_9 = 'LMN0P' # Are we all in the alphabet
# print(ex_9.isalpha()) #looks like an O but is actually a zero



# isdecimal() Are all characters decimals?

test_5 = '1234P'
test_6 = '234567'
# print(test_5.isdecimal()) #false because P isalpha
# print(test_6.isdecimal())


ex_11 = '123456' # Check for decimals?
# print(ex_11.isdecimal())


# isdigit() Are all characters digits?

test_7 = 'H1234' #has a word in here
test_8 = '9876'
# print(test_7.isdigit())
# print(test_8.isdigit())


ex_10 = '123Hello' # Check for digits!
# print(ex_10.isdigit())


''' Fun fact isdecimal() method supports only Decimal Numbers. isdigit() method supports Decimals, Subscripts, Superscripts. 
isnumeric will check for unicode characters
'''


# islower() Lets check for lowercase

test_9 = 'Zebra'
test_10 = 'affordable'
# print(test_9.islower()) #is this lower?
# print(test_10.islower())

ex_12 = 'Username' # check if all lowercase
# print(ex_12.islower()) #False because not ALL lowercase


# isupper() lets check for ALL uppercase
test_11 = 'Marshall'
test_12 = 'HALLOWEEN'
# print(test_11.isupper()) #false because only one uppercase character
# print(test_12.isupper())

ex_13 = 'TEMPLE' # check if uppercase
# print(ex_13.isupper())



# isspace() Lets check for whitespace (someone enters nothing for an input)
#if someone inputs nothing or a bunch of spaces

test_13 = '    '
test_14 = 'j      b    c'
# print(test_13.isspace())
# print(test_14.isspace()) #even if spaced out, returns False because there are characters

ex_14 = '   ' # check if whitespace
# print(ex_14.isspace())


# istitle() Let's check for title case

test_15 = 'Eye of the tiger'
test_16 = 'Eye Of The Tiger'
# print(test_15.istitle())
# print(test_16.istitle())

ex_15 = 'Tempus Fugit' # check for title casing
# print(ex_15.istitle())


# join() Joins the elements of an iterable to the end of the string

my_colors = ['blue', 'green', 'red', 'orange', 'blue']
# new_string = '-'.join(my_colors) #don't forget that join takes a parameter
# print(new_string)

ex_16 = ['summer', 'spring', 'fall', 'winter'] # create a string from this list and separate it with an asterisk
# new_string_2 = '*'.join(ex_16)
# print(new_string_2)



# lower() Converts a string into lower case
# day = 'MONDAY'
# print(day.lower())
# '''OR FOR READABILITY:'''
# new_day = day.lower()
# print(new_day)




# partition() Returns a tuple where the string is partitioned into three parts
test_17 = 'I am excited about spring time.'
# print(test_17.partition('about'))
# print(test_17.partition('spring'))

ex_17 = 'We will be going to the park next week.' # partition this string on the word 'going'

# replace() Returns a string where a specified value is replaced with a specified value


ex_18 = 'Today is Tuesday. Tuesday we play golf.' # replace instances of Tuesday with Thursday


# split() Splits the string at the specified separator, and returns a list
test_18 = 'I will be broken up on every space'


ex_19 = 'Split*me*up*on*the*asterisk' # split this spring up on every asterisk

# splitlines() Splits the string at line breaks and returns a list
lyrics = "Every time that I look in the mirror\nAll these lines on my face getting clearer\nThe past is gone\nOh, it went by like dusk to dawn\nIsn't that the way?"


# startswith() Returns true if the string starts with the specified value

name = 'giraffe'
# print(name.startswith('b'))

ex_20 = 'summer' # Check if this string starts with an 's'
# print(ex_20.startswith('s'))



# strip() Returns a trimmed version of the string
# username = '   jessica123    '
# clean_username = username.strip() #we are creating a variable for our strip method
# print(clean_username)


ex_21 = '  sportsfan876  ' # sanitize this string
# clean_ex = ex_21.strip()
# print(clean_ex)

'''What is user input'''
# user_input = input('What is your name? ')
# print(user_input)

'''number values with user input'''
# user_input = input('What is your favorite number? ')
# # print(user_input)
# # print(type(user_input)) #all user inputs are strings. we need to cast to integer
# '''you always have to create a new variable to cast to an integer'''
# num_input = int(user_input)
# print(num_input)
# print(type(num_input))



'''
Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True
'''

# Get input from user
# user_input = input('Please enter your number: ')
# # print(user_input)

# # Test input
# result = user_input.isdigit()
# print(result)

# # Provide output

# print('Is your input a number or not? ',result)
'''FORMATTED STRING'''
# print(f'Is {user_input} a number or not?', result)



'''
Take a word from the user. Then take a number from the user. Then print whether the word is longer than the number.

Examples:
apple
6
False

python
4
True
'''

# Get user input
# user_word = input('Please insert your word: ')
# user_number = int(input('Please insert your number: ')) #always try to cast to integer at the start

# print(user_word)
# print(user_number)

# Convert where needed
# length_of_word = len(user_word)

# print(length_of_word)
# print(length_of_number)

# Comparison
# compare = length_of_word > user_number
# print(compare)

# Output
# print(f'Is {user_word} longer than {user_number}?',compare)




















