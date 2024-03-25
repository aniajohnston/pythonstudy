import pandas as pd #alias
import numpy as np


''' Here's a neat trick '''

# This list contains 25, 1's.
lst_1 = [1,2, 3] * 25
# print(lst_1)

''' Lists part 2, lists within lists  '''

# 2 dimensional list
two_dimensional_list = [["hello", "bye"], [1, 5]]

# access hello
# print(two_dimensional_list[0][0])

# access bye
# print(two_dimensional_list[0][1])

# access 1
# print(two_dimensional_list[1][0])

# access 5
# print(two_dimensional_list[1][1])


# Access all the elements in this list with bracket notation
my_list = ["hello", 1, ["dog", 3], "cat", [True, ["frog", 5]]]

# Access Hello
# print(my_list[0])


# Access 1
# print(my_list[1])

# Access Dog
# print(my_list[2][0])

# Access 3
# print(my_list[2][1])

# Access Cat
# print(my_list[3])


#Access True
# print(my_list[4][0])

#Access Frog
# print(my_list[4][1][0])

#Access 5
# print(my_list[4][1][1])


# Nested Loops
#we broke this one down visually into rows and columns
#aka a matrix
mdList = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# regular loop
# for m in mdList:
#     print(m)

# Access individual values in list with nested loops
# for m in mdList: #access the first dimension
#     for p in m: #access the second dimension
#         print(p) #prints one through nine individually

''' Exercise
Write a 2D list that is a 3x3 grid of numbers.
Write some code that prints out that grid nicely with proper formatting.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 2 3
4 5 6
7 8 9

We know that this output is second dimension

'''

lis = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# for l in lis:
#     for n in l:
    #format as directed
        # print(n, end=' ') #the end parameter is an optional parameter in our print built-in function #adds space between our integers
    # print() #adds carriage return #think about empty print parameter... default is to create a new line

'''
Write some code that goes through a 2D list and prints the columns.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 4 7
2 5 8
3 6 9
Hint: First create a new 2D list with swapped rows and columns. (You will need 2 nested for loops.) Then it's the same as the last problem.
'''

lis = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

lis_2 = [] #creating a new list


# For loop transposes
# for i in range(len(lis[0])):
#     # print(i) #tells us the amount of columns we're gonna have
#     row = [] #create a second list, a temp holding place for integers
#     for item in lis:
#         # print(item[i]) #the columns 
#         row.append(item[i]) #here is where swapping happens
#     lis_2.append(row) #this will capture the swapped data
# print(lis_2) #this is the new and swapped list
    
#unpacking with star operator - Annie's solution
# for l in lis_2:
    # print(*l)

# For loop formats transposing - traditional method
# for rows in lis_2:
#     for columns in rows:
#         print(columns, end=' ')
#     print()

# With Pandas
#data frame method and we pass lis into it
df = pd.DataFrame(lis)
# print(df) #automatically indexes with a column header and a row header
transposed_list = pd.DataFrame(df).transpose().values.tolist() #transposing then converting to a list
# print(transposed_list)

# print in for loop for print's carriage return 


# With numpy
transposed_list = np.transpose(lis)
# print(transposed_list)


'''
You are given a 2D list representing a table of data with rows and columns. Write a Python program to calculate the sum and average of each column in the table.
For example, if this is your list:
data = [[45,56,89],[67,34,78],[23,67,34]]
This would be your output:
Column 1: Sum = 135, Average = 45.0
Column 2: Sum = 157, Average = 52.33
Column 3: Sum = 201, Average = 67.0
Hint: Make a list to store the sums, and a list to store the averages.


'''

data = [[45,56,89],
        [67,34,78],
        [23,67,34]]

data_columns = []

# Transpose data
# for i in range:
#     for my_columns in data:

# Format for output


# List Comprehension

# For Loop
# Add veggies less than 6 letters to new list
vegetables = ['broccoli', 'kale', 'onion', 'garlic', 'kale']


# List comprehension
vegetables = ['broccoli', 'kale', 'onion', 'garlic', 'kale']


''' Exercise
You are given a list of integers. Write a Python program to create a new list that only includes the even numbers from the original list.
You can do this in one line with a list comprehension.
Example:
original_list = [34, 57, 81, 92, 2, 13]
new_list = [34, 92, 2]
'''

''' List comprehension for conditions'''
# With a For Loop
original_list = [34, 57, 81, 92, 2, 13]
new_list = []



# With list comprehension
original_list = [34, 57, 81, 92, 2, 13]



''' List comprehension with expressions'''

# Lets add 5 to every item in this list
numbers = [0, 2, 3, 8, 9, 11, 20]


# We can add two lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]



# Multiply items from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]



'''
Exercise

You work for a sales company and must generate a list of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a list of customers over 60, and a list of customers who have made at least 5 purchases. Use a list comprehension to output a list of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']
Output: ['Dominic', 'Simone']

'''

over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']

customer_discount = []

# For Loop

# List comprehension
