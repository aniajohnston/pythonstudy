import numpy
import pandas

''' Here's a neat trick '''

# This list contains 100, 1's.
#concetenate a list and populate it with an item
# lst_1 = [1]*100
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

# Access True
# print(my_list[4][0])

# Access Frog
# print(my_list[4][1][0])


# Access 5
# print(my_list[4][1][1])


# Nested Loops
# mdList = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# regular loop
# for m in mdList:
#     print(m)

# Access individual values in list with nested loops
# for m in mdList:
#     for w in m:
        # print(w) #reaching into each list to pull data individually

lis = [[1,2,3],[4,5,6],[7,8,9]]

# Iterate through each list inside the 'lis' list
for l in lis:
    # Iterate through each element inside the current list 'l'
    for i in l:
        # Print each element followed by a space instead of a newline
        print(i, end=' ')
    # After printing all elements of the current list, print a newline
    print()

'''Great YouTube Video: https://www.youtube.com/watch?v=t2pG7tyHEPc'''

# print('hello',end=' ')
# print('world')
