class Employee:
    '''Employee Management System
    5 Attributes: name, job title, department, salary, hire year'''
    
    #Initialization
    def __init__(self, name, job_title, department, salary, hire_year):
        #connect user data to self to access anywhere
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    #String Representation
    def __str__(self):
        return f"{self.name} is a {self.job_title} and works in the {self.department} department with a salary of ${self.salary} and was hired in {self.hire_year}."

    #Years Worked - Total years this employee has worked here, based on the hire year

    #Total Expenses - Total salary expenses for this employee, salary times years worked

    #Write - Write your employee info to a text file

    #Accessor

    #Mutator
    
    pass

'''Type Hinting and a Doctring Example'''
# def net_worth(assets: float,liabilities:float) -> float:
#     '''return networth
#     -user's assets
#     -user's liabilities'''
#     return assets - liabilities 

employee1 = Employee("Rob","Programmer","Tech",50000,2000)
print(employee1)