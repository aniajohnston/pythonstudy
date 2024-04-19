from statistics import mode
import pandas as pd
import numpy as np

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions
    -keys need to be strings with _ or space OR integers

'''

# How do we create a dictionary?

user_data = {"user id":400, 
             "name":"Fritz",
             "address": "1515 Mockingbird Lane"}

# print(user_data)
# print(type(user_data)) # curly brackets with nothing inside automatically imply dictionary



# Access keys with brackets
# print(user_data['name'])
# print(user_data['user id'])
# print(user_data['address'])


# Add new key value pair
# you won't get duplicates, if you change 'state' to 'NJ' and you call for 'state' 'NY' is gone.

user_data['state'] = 'NY'
# print(user_data)
# print(user_data['state']) #calling for state


# lets look at all the methods available to us

#directory method
# print(dir(user_data)) #prints all the methods available to us in the dictionaries class

# lets try one

#__contains__ - returns True or False if it contains the key
# print(user_data.__contains__('user id'))
# print(user_data.__contains__('city'))




# Dict constructor

#declaring an empty dictionary
new_dictionary = dict() #this is called the dictionary constructor

# print(new_dictionary)
# print(type(new_dictionary))

pet_name = dict(name='Fido', age = 14)
# print(pet_name)
# print(type(pet_name))

#actually creates a dictionary and appends the key value pairs



# Dictionary methods


dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use the keys methods to get just the keys from this dictionary
# Assign keys to a variable
# dog_information = dog.keys() #does not need a parameter
# print(dog_information)
# print(dog.keys())


# Lets use clear method to remove all elements
# dog.clear()
# print(dog)



# Lets use get method to get the value of a key
# age = dog.get('age')
# print(age)


# # # lets look at one of the parameters to show an error if the key doesnt exist
# print(dog.get('temperament', 'Key does not exist.')) #parameter, seperated by a comma, lets you print a specific error

# Lets create a copy
# dog_copy = dog.copy()
# print(dog_copy)
# print(type(new_dog))

# Lets remove a specified key with pop
# dog_copy.pop('breed') #removing breed key value pair
# print(dog_copy)


# Lets remove a last inserted key-value pair with popitem
# takes out the most recent entry
# dog_copy.popitem()
# print(dog_copy)

# Get a list with each key-value pair with items
# will return a list of tuples
# key_value_pairs_in_a_list_of_tuples = dog_copy.items()
# print(key_value_pairs_in_a_list_of_tuples)

# we can loop through
# loops through the key and matching value using the items() method.
# for k, v in dog_copy.items():
    # print(k,v)



dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Update allows us to update by changing and adding data
# dog.update({'temperament':'happy','breed':'chihuahua'})
# print(dog)








# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}
 
# print(list1[3])
# print(list1[3])

#updating key value pairs

list1[3] = 'z'
dict1[3] = 'z'

# print(list1)
# print(dict1)

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
new_dict = {}

# for n in range(len(list1)): #we can use list1 or list2 because range for both is 3
#     new_dict.update({list1[n]:list2[n]})
# print(new_dict) #if the print statement was in the loop we can see the dictionary growing


my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# Using Zip & Dict
# my_dictionary = dict(zip(my_keys,my_values))
# print(my_dictionary)


# Using dictionary comprehension
my_dictionary = {keys: values for (keys,values) in zip(my_keys,my_values)}
# print(my_dictionary)


'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''

words = {"color":"blue", "veggie":"radish", "vehicle": "bike", "mood": "happy", "pet":"cat"}

# print(words.items()) #returns dict_items

#printing the words one at a time

# for w,c in words.items():
#     print(w,c)


# As datasets, we can use bracket notation to taget items

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}

# print(choices['flavors'][0])
# print(choices['sizes'][1])

'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''

cars = {"make":"honda", 
       "model":"accord", 
       "year":2011 , 
       "number of doors":4,
       "cylinders": 6}

# print(cars.items())

'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

'''CHALLENGING'''
my_list_items = [1,2,4,1,3,4,1,1] # our list

# output = dict() #my final output

# for m in my_list_items:
#     if m not in output:
#         output[m] = 1 #add it initially
#     else:
#         output[m] += 1
# print(output)
#first number is value second number is the amount that it appears


#shorten the syntax
# for m in my_list_items:
#     output[m] = my_list_items.count(m)
# print(output)

# Statistics module
use_stats_module = [1,2,4,1,3,4,1,1]
result = mode(use_stats_module)
# print(result)



# Looping through and adding 
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

sum = 0.00

# for v in incomes.values():
#     sum += v
# print(sum)
    


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




 



