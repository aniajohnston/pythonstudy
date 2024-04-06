'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.

Dictionaries also have curly brackets, only use parens to initialize
'''

# Ways to create a set
empty_set = set() #initialize a set
# print(empty_set)
# print(type(empty_set))

# What am I?
empty_dict = {} #this initializes a dictionary
# print(empty_dict)
# print(type(empty_dict))

# Pass in a list
colors = ['black', 'blue', 'orange','yellow']
set_of_colors = set(colors)
# print(colors)
# print(type(colors))

# print(set_of_colors)
# print(type(set_of_colors))

# Unordered
animals = set(['panda', 'lion', 'koala', 'tiger'])
# print(animals)
# unordered is faster, there's no memory allocation.

# Unchangeable
animals = set(['panda', 'lion', 'koala', 'tiger'])
# animals[2] = 'bear'
# TypeError: 'set' object does not support item assignment
# print(animals)

# Unindexed
animals = set(['panda', 'lion', 'koala', 'tiger'])
# print(animals[0])
# TypeError: 'set' object does not support item assignment

# Break up a string
first_name = set('Ania')
# string in initialization
#result= {'i', 'n', 'a', 'A'}

last_name = {'Johnston'}
# print(last_name)
#captures one value: {'Johnston'}

# No duplicates allowed
months = set(['January', 'January','January', 'Feb', 'March','April'])
# print(months)
# output: {'Feb', 'January', 'April', 'March'}
# No duplicates - How did we solve this problem before?

'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
''' With a for loop and appending'''

#original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# # this will capture our unique states
no_dupes = []
# #we will loop through states_backup, and append only the first occurence of each state into
# for s in states:
#     if s not in no_dupes:
#         no_dupes.append(s)
# print(no_dupes)


''' With sets and returning a list '''

states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']
new_list = list(set(states)) 
# print(new_list)
