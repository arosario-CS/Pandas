
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

"""read each row"""
#print(dataframe.iloc[2])

"""
read a specific location (X,Y), in this example it is the 
data on the index position 2 (row2) and the 1st piece of data on that row.
"""
#print(dataframe.iloc[2,1])

"""iterating through each row and sorting"""
#for index, row in dataframe.iterrows():
    #print(index, row)

#for index, row in dataframe.iterrows():
    #print(index, row ['Name'])

#print(dataframe.loc[dataframe['Type 1'] == "Fire"])

"""
sorting and describing data
shows mean, std, min, max, and more useful information dealing with statistics
"""
#print(dataframe.describe())
#print(dataframe.sort_values("Name"))
#print(dataframe.sort_values("Name", ascending= False))
#print(dataframe.sort_values(["Type 1", "HP"]))
#print(dataframe.sort_values(["Type 1", "HP"], ascending= [1,0]))

"""
Making changes to data
"""
#dataframe['Total'] = dataframe['HP'] + dataframe['Attack'] + dataframe['Defense'] + dataframe['Sp. Atk'] + dataframe['Sp. Def'] + dataframe['Speed']
#dataframef = dataframe.drop(columns=['Total'])
#dataframe['Total'] = dataframe.iloc[:, 4:10].sum(axis=1)

"""
saving data to a new file, naming it and adjusting it
"""
#dataframe.to_csv('modified.csv', index=False)
#dataframe.to_excel('modified.xlsx', index=False)
#dataframe.to_csv('modified.txt', index=False, sep='\t')

"""
filtering data aka setting conditions
"""
#new_df = dataframe.loc[(dataframe['Type 1'] == 'Grass') & (dataframe['Type 2'] == 'Poison') & (dataframe['HP'] > 70)]
#new_df.reset_index(drop=True, inplace=True)
#new_df.to_csv('filtered.csv')
#dataframe.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']