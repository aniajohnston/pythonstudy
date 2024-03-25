''' Strings Part 2'''

# Strings are immutable
''''''
str_1 = 'BLUE' 
str_1.lower()
# print(str_1.lower()) #the change itself works (aka line six, but can't work when it is just the variable)
# print(str_1) # .lower string method has not changed string, it doesn't work here

str_1 = str_1.lower()
# print(str_1)  # new string with lower method works :)

day = '  TUESDAY   ' # Create a new string with no whitespace 
new_day = day.strip()
# print(day)
# print(len(day)) #this is OUR form of testing - analytical
# print(new_day)
# print(len(new_day)) #this is OUR form of testing - analytical




'''Indexing, with square brackets'''
'''BRACKET NOTATION - ALWAYS zero indexing, the first letter is always 0'''
'''Ex: 'J' in Jasmine is at position zero'''
word = 'Jasmine'

# print(word[0]) #here it is not assigned to a variable
# first_letter = word[0] #assign to variable
# print(first_letter) #print variable
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])
# print(word[6])
# print(word[7]) # Lets note the error 'IndexError: string index out of range'

# Create a variable to capture the first letter of this string
greeting = 'hello'
first = greeting[0] #variable goes into () then bracket notation
# print(first)



'''Len() function and bracket notation'''
last_position = greeting[len(greeting)-1] # Grabbing the length minus 1 and applying to the string will get the last position
# print(last_position)

# Using the length and bracket notation, access the last letter in the variable below
month = 'February'
last = month[len(month)-1]
# print(last)

#print the second to last
second_last = month[len(month)-2]
# print(second_last)


# Using bracket notation access the letter x, the letter e, and the letter d 
first_name = 'Alexandra'
x = first_name[3]
e = first_name[2]
d = first_name[len(first_name)-3]
other_d = first_name[6]
# print(x)
# print(e)
# print(d)
# print(other_d)




'''Reverse indexing'''
fav_animal = 'Ostrich'

# print(fav_animal[-1])
# # print(fav_animal[-2])
# # print(fav_animal[-3])
# # print(fav_animal[-4])
# print(fav_animal[-5])
# # print(fav_animal[-6])
# print(fav_animal[-7])
# print(fav_animal[-8]) # Lets note the error 'IndexError: string index out of range'

# Using bracket notation and reverse indexing, access the letter g, the letter i, the letter p
fav_season = 'spring'
letter_g = fav_season[-1]
letter_i = fav_season[-3]
letter_p = fav_season[-5]

# print(letter_g)
# print(letter_i)
# print(letter_p)

g = fav_season[5]
i = fav_season[3]
p = fav_season[1]

# print(g)
# print(i)
# print(p)


''' Slicing '''
# There are 3 parameters available with indexing with bracket notation [start:stop:step]
fav_food = 'spaghetti'
slice_of_fav_food = fav_food[2:6] #excludes character that you stop at
# prediction: 'aghe'
# print(slice_of_fav_food)

# Using slicing please create a string that accesses 'rica' in 'America'

country = 'America'
slice_of_country = country[3:7]
# print(slice_of_country)

# Using slicing please create a string that accesses 'ora' in 'Dora the explorer'
cartoon = 'Dora the explorer'
slice_of_cartoon = cartoon[1:4]
# print(slice_of_cartoon)

# Using slicing please create a string that accesses 'explo' in 'Dora the explorer'
second_slice_cartoon = cartoon[9:14]
# print(second_slice_cartoon)

# Using slicing please create a string that accesses 'albo' in 'Rocky Balboa'
boxer = 'Rocky Balboa'
slice_boxer = boxer[7:11]
# print(slice_boxer)

'''STEPPING'''
# Let's step through this string 2 characters at a time
superheroine = 'Wonder Woman'
# print(superheroine[2:len(superheroine):2]) #start stop and step through

# print(superheroine[0:len(superheroine):2])
# prediction: Wne oa

# Lets step through this entire word and skip by 4
word = 'Supercalifragilisticexpialidocious'
# print(word[0:len(word):4])



'''Slicing in reverse '''
random_word = 'daycare' # Excludes the start character
"""IF A WORD NEEDS TO BE SET IN REVERSE:"""
# print(random_word[::-1]) # Full daycare in reverse

'''FOCUS ON THIS it is tricky'''
# print(random_word[5:0:-1]) # racya
# step 1: count backwards 5 excluding zero
# step 2: include the word you stopped at 
#why does it exclude e?
#because it excludes the start character


# print(random_word[6:0:-1]) #eracya
#why does it exclude d?
#

'''
Write some code to print the second half of a string.


Example:
python
hon

'''
word = 'python'

#create variable
word = 'python'
#create a variable for half of word
half = int((len(word) / 2)) #len was a float but we need an integer
# print(half) #test

#Create final bracket notation
new_word = word[half:len(word)] #first half : rest of word
# print(new_word)

"""Shortened form"""
# print(word[int((len(word) / 2)):len(word)]) #start parameter : end parameter







'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
# email = input('Hello, please enter your email address: ')
# print(email)

# Sanatize data
# email = email.strip()
# print(email)

# Test 1: It has a "." at the third-to-last index
# test_1 = email[-4] == '.'
# print(test_1)
# print('Does it have a "." at the second to last index?',test_1)


# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier

# Test 3: There is at least one character before the "@" symbol

# Test 4: It doesn’t have any spaces (doesn’t contain " ")

#Final Test with and Keyword


# End Parameter
# print('Hello', end=' ')
# print('World', end='')
# print('!', end='\n')


# Sep Parameter
# print("Today I woke up at ", 8, " am", sep='*')

'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''
# userin = input("Please enter your input: ")

# Formatted strings

long_num = 12.34567890

'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342



'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''
