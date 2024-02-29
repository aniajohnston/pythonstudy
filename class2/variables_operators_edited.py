# Print built in function
# print('Hello World!') #string can have single or double quotes #hardcoded

#using variable
# greeting = 'hello world '
# print(greeting)

# first_name = 'Ania'
# print(first_name) # the variable is not hard-coded. 

# print(greeting + first_name) #you can add two of the same data type. Concatination

# Addition
# print(4+2)
# print(5+5)
# print(100+5)

# Subtraction
# print(10-3)
# print(4-3)
# print(10-5)


# Multiplication
# print(3*3)
# print(2*8)
# print(5*7)

# Division
# print(10/2)
# print(5/3)
# print(5/0) #ZeroDivisionError: division by zero

#try except
# try:
#     print(5/0)
# except ZeroDivisionError as e:
#     print('You cannot divide by zero, have a great day!')

# Exponents
# print(5 ** 5)
# print(2 ** 5)
# print(3 ** 6)

# Integer Division
# print(10 // 3) #whole number with no remainder
# print(4 // 3) #should be '1' because 3 goes into 4 only once.

# Modulo/Mod/Remainder
# print(5 % 2) #the remainder is 1 #helps you solve if a number is even or odd.
# print(10 % 4) #the answer should be 2
# Program to find the perimeter of a rectangle

# Program to find the perimeter of a rectangle
# Perimeter = 2* (length + width)

# length = 10
# width = 7

# perimeter = 2 * (length + width)

# print(perimeter)


# Data Types


# Integer
# num_one = 5
# print(num_one)
# print(type(num_one))

# String
# string_one = 'this is a string'
# print(string_one)
# print(type(string_one))

# Bool
# technical_errors = True
# print(technical_errors)
# print(type(technical_errors))

# Float
# num_two = 1.22
# print(num_two)
# print(type(num_two))

# String addition
# first_name = 'Ania'
# last_name = 'Johnston'
# fullname = first_name + ' ' + last_name
# print(fullname)
# print(first_name, last_name)


# List 
# student_grades = [100, 95, 70, 85, 40] #always in brackets
# print(student_grades)
# print(type(student_grades))

#Quick for loop
# for s in student_grades: #the letter iterates through the list. could be anything but s here stands for student grades.
#     print(s)



# Dictionary
# demographic_info = {"First Name": "Ania",
#                     "Last Name": "Johnston",
#                     "State": "New York"}
# print(demographic_info)
# print(type(demographic_info))


# Cast a string to an integer
# my_string = '6'
# new_number = int(my_string) #casting a string to an integer
# print(new_number)
# print(type(new_number))


# Cast integer to string
# my_number = 6
# new_num = str(my_number) #called a 'stir'
# print(type(new_num))

# Fav Colors
# colors = ['blue','green','red','brown'] #this list item has four elements
# num_colors = len(colors) #calculates how many elements are in your list
# print(num_colors)

#can also count letters
# color = 'orange'
# # count = len(color)
# # print(count)


# for loop
# for c in color:
#     print(c)


# finding amount of assignments


# Perimeter of a rectangle


# Determine perimeter and display output


# Fahrenheit to Celsius
# F = 89
# C = ((F -32)* 5/9)
# print(C)



# Eval let's you get a boolean value if true or false.
# cold_weather = 'True'
# print(eval(cold_weather))

'''
# You are given a triangle with a side #1 of 4, base of 6, and side #2 of 3. Create
a brief python script that will determine the perimeter of the triangle. Comment your code

perimeter = a + b + c

1. Print the perimeter
2. Using boolean operators is side #1 greater than the base?
3. Using boolean operators is side #2 less than the base?
4. Using boolean operators is base larger than or equal to side #1?
'''
side_1 = 4
side_2 = 3
base = 6
perimeter = side_1 + side_2 + base
print(perimeter) #1.

greater = side_1 > base
print('Using boolean operators is side #1 greater than the base?',greater) #2.

less = side_2 < base
print('Using boolean operators is side #2 less than the base?',less) #3.

greater_eq = base >= side_1
print('Using boolean operators is base larger than or equal to side #1?',greater_eq) #4.






