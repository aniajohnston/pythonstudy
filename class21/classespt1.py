from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer (class definition and name of our class)
#camel case, first letter caps
class Point2d:
    '''Initializer'''
#builds the object
    def __init__(self, x=0, y=0):
        self.x =x
        self.y =y

    '''String Representation - control what happens when someone uses print()'''
    def __str__(self):
        return f'({self.x},{self.y})'
    
    '''add your object to another object of your class 
        - functions within a class are called methods'''
    def __add__(self,other):
        return Point2d(self.x + other.x, self.y + other.y) 

    '''subtract object from another object'''
    def __sub__(self,other):
        return Point2d(self.x - other.x, self.y-other.y)
    
    '''Test equality between this object and another'''
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
        
    '''Less than function'''
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False

    '''Mutator Method - Setter X
        - allows us to change attributes to our class objects
        - allows user of the class to change the value of x if they needed to
        '''
    def set_x(self, new_x):
        self.x = new_x
    '''Setter for y'''
    def set_y(self,new_y):
        self.y = new_y

    '''Accessor Method for x'''
    def get_x(self):
        return self.x
    '''Accessor Method for y'''
    def get_y(self):
        return self.y

#creating an object of the Point2D class 
point1 = Point2d(4,10) 
point2 = Point2d(8,15)



# Return a string representation of this object
# print(point1) 
# print(point2) 
    
# Adds this object to another object from the same class, return a new object.
# print(point1 + point2)
    
# Subtracts another object from this object, return a new object.
# print(point1 - point2)


# Test equality between this object and another, return a boolean.
point3 = Point2d(3,4)
point4 = Point2d(3,4)
# print(point3 == point4)
# print(point4 == point4) #before using __eq__ only this would be True
    
# Less than method
point5 = Point2d(10,12)
point6 = Point2d(13,15)
# print(point5 < point6)


# Mutator method for x
point7 = Point2d(5,11)
point7.set_x(10) #our method will change the value of x
# print(point7)

# Mutator method for y
point7.set_y(25) #our method will change the value of y
# print(point7)


# Accessor method
# print(point7.get_x())
# print(point7.get_y())

'''Exercise - Dog Class
This class will take 3 parameters, dog name, dog breed, and age (human years)'''

class Dog:
    #declare the 3 parameters
    def __init__(self, name, birth_year, breed):
        #connect user data to self to access them anywhere
        self.name = name
        self.birth_year = birth_year
        self.breed = breed
    
        #create a string represenation for the user 
    def __str__(self): #self allows us to use this globally
        return f'{self.name} is a {self.breed} and was born in {self.birth_year}.'

    #method that finds the human age
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        #DO NOT use formatted string if planning to reference
        return year - self.birth_year

    #LONG method to find dog years
    # def dog_year(self):
    #     today = datetime.datetime.now()
    #     year = today.year
    #     return f'{self.name} is {(year - self.birth_year)*7} years old in dog years.'

    #SHORT method to find dog years via calling function within class using self
    def dog_year(self):
        #assign to variable
        dog_years = 7 * self.human_age()
        #create return
        return f'{self.name} is {dog_years} in dog years.'
    
#our dog objects
dog1 = Dog("Fido",2020,'Golden Retriever')
dog2 = Dog("Zuzu",2021, 'Dachsund')
dog3 = Dog("Stella", 2016, 'Japanese Chin')

#printing our dog objects
# print(dog1)
# print(dog2)
# print(dog3)

#testing our date and time module
# today = datetime.datetime.now()
# year = today.year
# print(year)

#printing our human age
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())

#printing our dog years
print(dog1.dog_year())
print(dog2.dog_year())
print(dog3.dog_year())




''' Exercise - Date Class '''




 




'''
Exercise - Dog Class
'''






