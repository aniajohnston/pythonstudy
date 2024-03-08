'''Pandas creates a dataframe from the JSON
can also do CRON jobs'''

'''as pd is an alias that allows the syntax to be shortened 
- you don't need to write pandas everytime just pd'''


'''You can obtain data from somewhere as a list then you can 
import it to Python, do something with that list and then export
it to a CSV'''

'''CSV stands for comma seperated values, they can be imported into excel
stores tabular data in text format. Best viewed in a spreadsheet program
Can be seen by a notepad or text editor as fields seperated by commas'''

import pandas as pd # Import from pandas library

animals = ['Lions','Tigers','Bears','Dogs','Cats'] #list collection

#convert to a format that Pandas can use
df = pd.DataFrame(animals)
# print(df)

#the dot lets us access the methods that Pandas has
df.to_csv('output.csv') #this will give us our output in Class3 folder

'''Parameters need arguments'''