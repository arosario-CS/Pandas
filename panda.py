
""" 
importing panda and giving it a name so we can call it as pd 
"""
import pandas as pd

""" 
reading different files into the program
these paths work because the files are in the same folder that we are working in.
A delimiter is used to when you have data seperated by commas or such you would do 
, delimiter = ',' and it will seperate the data for you
"""
dataframe = pd.read_csv('pokemon_data.csv')
#dataframe_xlsx = pd.read_excel('pokemon_data.xlsx')
#dataframe_txt = pd.read_csv('pokemon_data.txt', delimiter= '\t')

"""
.head lets you see top x amount of rows
.tail bottom x amount of rows
"""
#print(dataframe.head(3))
#print(dataframe_xlsx.head)
#print(dataframe_txt)

"""read headers"""
#print(dataframe.columns)

"""read each column or multiple columns"""
#print(dataframe['Name'])
#print(dataframe[["Name", "Type 1", "HP"]])