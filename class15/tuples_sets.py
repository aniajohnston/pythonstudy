''' Tuples & Sets '''

'''
Fun Facts about Tuples
    -ordered and unchangeable (example, storing a username and password, storing an RGB value that must not change)
    -can't add or remove items
    -round brackets
    -faster than lists
    -used to store constants
    -used heterogeneous data structures (integers, floats, strings, etc) for example someone's age, gender and last name, (15, 'M', 'JONES')
    -heterogenous data structures save memory. why? lists need to over-allocate to account for new elements
    -readability
    -lets the programmer or other programmer know, this data collection should not be altered
'''

my_first_set = set()
# print(type(my_first_set))

this_is_a_tuple = 5, 'Annie', 'Eclipse'
# print(this_is_a_tuple)
# print(type(this_is_a_tuple))

# Count & Indexing

my_number_tuple = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10)

# Use the count Tuple method to count how many instances we have for 2, 3, 8, 9, 10

# print(my_number_tuple.count(2))
# print(my_number_tuple.count(3))
# print(my_number_tuple.count(8))
# print(my_number_tuple.count(9))
# print(my_number_tuple.count(10))


my_letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
# Use the index tuple method to return the position of letters b, d, f, h, and i

#index of position
# print(my_letter_tuple[1])
# print(my_letter_tuple[3])
# print(my_letter_tuple[5])
# print(my_letter_tuple[7])
# print(my_letter_tuple[8])

#position of index
# print(my_letter_tuple.index('b'))

# Unpacking
user = ('Joe', 'Smith', 24)
fname, lname, age = user
# print(fname)
# print(lname)
# print(age)

colors = 'blue', 'green', 'red'
bl, g, r = colors
# print(bl)
# print(g)
# print(r)


# Loop through list of Tuples

weekdays = [("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6), ("Sunday", 7)]



# for day, number in weekdays: looping through our list of tuples, day = Monday, num = 1
#     print(f'{day} is day {number} of the week.')



# Adding tuples
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)

third_tuple = first_tuple + second_tuple
# print(third_tuple)

'''
You have a tuple of numbers:
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
You have a tuple of months:
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
Use these tuples to make a list of tuples where each tuple contains a number and the month it corresponds to, like this: [("January",1),...,("December",12)]
Now print each month and its number using tuple unpacking in a for loop. The first line of output should look like this:
January is month 1 of the year.
'''
# months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
# numbers = (1,2,3,4,5,6,7,8,9,10,11,12)

# # Create List of Tuples
# calendar = []

# for n in range(len(numbers)):
#     calendar.append((months[n], numbers[n]))
# # print(calender)

# # Use a for loop to unpack and generate strings
# for m, n in calendar:
#     print(f'{m} is month {n} of the year.')


'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.

'''


# Ways to create a set
i_am_empty = set() #curly brackets would be a dictionary for initialization. otherwise sets are curly brackets
# print(i_am_empty)
# print(type(i_am_empty))

# What am I?
check_my_type = {}
# print(type(check_my_type)) # a dictionary

# Pass in a list
my_fav_colors_list = ['green', 'blue', 'red'] #converting this list to a set
my_fav_colors_set = set(my_fav_colors_list)
# print(type(my_fav_colors_set))
# print(my_fav_colors_set)

# Unordered
my_unordered_set = {'blue', 'green', 'red', 'orange'}
# print(my_unordered_set)

#change a value of a list with a bracket notation
dow = ['monday', 'tuesday','friday']
print(dow[1]) #returns tuesday
dow[1] = 'friday'
# print(dow)

# Unchangeable
my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}
# my_unchangeable_set[1] = 'to' #item assignment
# print(my_unchangeable_set) #TypeError: 'set' object does not support item assignment

# Unindexed
my_unindexable_set = {'I', 'cant', 'be', 'indexed'}
# print(my_unindexable_set[2]) #TypeError: 'set' object does not support item assignment


# Break up a string by casting to a set
first_name = set('John')
# print(first_name)



# No duplicates allowed, sets are unique
my_cars = {'chevy', 'toyota', 'ford', 'ford', 'honda', 'honda'}
# print(my_cars)


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

new_list = []

# for s in states:
#     if s not in new_list:
#         new_list.append(s)
# print(new_list)


''' With sets and returning a list '''

states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']
# print(list(set(states)))



# We can loop through sets
top_ten_movies = {'shawshank redemption', 'avatar', 'avengers', 'its a wonderful life'}

# for m in top_ten_movies:
    # print(m)
    # print(type(m)) #returns a string because they are all strings

# Let's add silver .add()
colors = {'blue', 'green', 'red'}
# colors.add('silver')
# print(colors)
# print(type(colors))


# Lets clear all our items .clear()
transportation = {'cars', 'bikes', 'plane'}
# transportation.clear()
# print(transportation)



# Lets create a copy .copy()
sitcoms = {'friends', 'seinfeld', 'honeymooners'}
comedy = sitcoms.copy()
# print(sitcoms)
# print(comedy)
#identify unique id
# print(id(sitcoms))
# print(id(comedy))


# Remove vermont from our set
states = {'california', 'new york', 'vermont', 'connecticut'}
states.remove('vermont')
# print(states)



# Difference - What's different? ( - or .difference())
student_set = {'oleg', 'anna', 'farley'}
student_set_2 = {'oleg', 'anna', 'brenetta'}
# result = student_set - student_set_2 
# result = student_set.difference(student_set_2)
#tells us the difference between the two sets, returns the only item that is different
# print(result)



# Intersect - What do we have in common?
# my_schedule = {'mon', 'wed', 'thurs'}
# dana_schedule = {'wed', 'fri', 'sat'}
# result = my_schedule & dana_schedule #operator
# result = my_schedule.instersect(dana_schedule) #method
# # print(result)




# Union - uniquely list every pet
sarah_pets = {'dog', 'cat', 'bird'}
isaiah_pets = {'chickens', 'dog', 'fish'}
khadaziah_pets = {'bird', 'dog', 'fish'}
brenetta_pets = {'turtle'}
# result = sarah_pets | isaiah_pets | khadaziah_pets | brenetta_pets #operator
# result = sarah_pets.union(isaiah_pets, khadaziah_pets, brenetta_pets) #method
# print(result)




# Symmetric difference - Items outside of matching items

my_books = {'catcher in the rye', 'richest man in babylon'}
her_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}

# result = my_books^her_books #operator
# result = my_books.symmetric_difference(her_books) #method
# print(result)



'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''

over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}

#solve old-fasioned way
# discounts = []
# for o in over_60_years:
#     if o in over_5_purchases:
#         discounts.append(o)
# print(discounts)

# Solve with an intersection - solve with 1 or 2 lines of code
# print(over_60_years&over_5_purchases)


'''
Exercise - Sets
See flowchart
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''

#Initialize our variables

#Data Collection Sets
python_devs, javascript_devs = set(), set()

#User Input
dev_type_input, dev_name_input = '', ''


# User Instructions
print('''
Python and JS Developer Tracker
Instructions
Input 's' or 'stop' at anytime to exit the program
To add a Python developer type 'p' when prompted.
To add a Javascript developer type 'js' when prompted.
       ''')

#Error messages
error_msgs = ('Invalid input, please try again','Thank you, have a nice day')

#while loop
while True:
    #inputs
    dev_type_input = input("Type 'P' for Python developer, 'JS' for JavaScript developer, or 'STOP' to exit the program: ").lower().strip()

    #if statements, break keyword, continue
    #this gives the user an exit
    if dev_type_input == 'stop':
        print(error_msgs[1])
        break
    #get a dev type, add to our sets, and offer an exit
    if dev_type_input == 'p' or dev_type_input == 'js':
        dev_name_input = input("Enter developer name: ").lower().strip()

        if dev_name_input == 'stop':
            print(error_msgs[1])
            break
        elif dev_type_input == 'p':
            python_devs.add(dev_name_input.title())
        else:
            javascript_devs.add(dev_name_input.title())
    else:
        print(error_msgs[0])
        continue

    #Set operations
    know_both = python_devs.intersection(javascript_devs) #everybody that knows both

    js_but_not_python = javascript_devs.difference(python_devs) #know js but not python

    know_python_or_js_but_not_both = javascript_devs.symmetric_difference(python_devs)

    #if sets are empty, display no data for user
    if know_both == set():
        know_both = 'No Data'
    
    if js_but_not_python == set():
        know_both = 'No Data'

    if know_python_or_js_but_not_both == set():
        know_python_or_js_but_not_both = 'No Data'

    #final print statement
    print('RESULTS')
    print('-----------------------------------------------------')
    print(f'The following developers know both languages: {know_both}')
    print(f'The following developers know JavaScript but not Python: {js_but_not_python}')
    print(f'The following developers know Python or Javascript: {know_python_or_js_but_not_both}')
    print('-----------------------------------------------------')
    













