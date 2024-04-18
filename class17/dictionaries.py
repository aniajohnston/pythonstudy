from statistics import mode
import pandas as pd
import numpy as np

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?




# Access keys with brackets


# # Add new key value


# lets look at all the methods available to us


# lets try one


# Dict constructor





# Dictionary methods


dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use the keys methods to get the keys from this dictionary
# Assign keys to a variable



# Assign values to a variable



# Lets use clear method to remove all elements



# Lets use get method to get a key value



# # # lets look at one of the parameters to show an error if the key doesnt exist

# Lets create a copy


# Lets remove a specified key with pop



# Lets remove a last inserted key-value pair with popitem


# Get a list with each key-value pair with items


# we can loop through


# Update allows us to update by changing and adding data


# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}
 

'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]



my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# Using Zip & Dict


# Using dictionary comprehension



'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''

words = {"color":"blue", "veggie":"radish", "vehicle": "bike", "mood": "happy", "pet":"cat"}



# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''

# car = {"make":"honda", 
#        "model":"accord", 
#        "year":2011 , 
#        "number of doors":4,
#        "cylinders": 6}

# print(car)

'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list


# Statistics module


# Looping through and adding 
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}



'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000},
           {'name': 'Joe', 'title': 'consultant', 'salary': 25000},\
           {'name': 'Susan', 'title': 'consultant', 'salary': 40000},
           {'name': 'Isaiah', 'title': 'sales', 'salary': 120000},\
           {'name': 'Brenetta', 'title': 'sales', 'salary': 150000}]

# Our output dictionaries
title_salary_dict = {} #capture our titles and salary totals
title_count_dict = {} #this will capture out title count

#loop through our list of dictionaries
for r in records:
    #define key and value pair for output
    title = r['title']
    salary =r['salary']
    #if the job title does not currently exist, we will add the title and the salary
    if title not in title_salary_dict:
        title_salary_dict[title] = salary
        title_count_dict[title] = 1
    else:
        # otherwise, we will update the salary, and update the titles 
        title_salary_dict[title] += salary
        title_count_dict[title] += 1

#let's take a look at our output
# print('All titles and sum of salaries', title_salary_dict)
# print('Titles, and the count of employees', title_count_dict)


result = {s:float(title_salary_dict[s])/title_count_dict[s] for s in title_salary_dict}

# print(result)

# Pandas solution
df = pd.DataFrame.from_records(records)
result = df.groupby('title')['salary'].mean()

# print(result)




 



