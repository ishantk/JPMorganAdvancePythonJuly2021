"""
    Pandas
        pip install pandas
        Panel Data
        Series      -> 1D
        DataFrames  -> 2D
        Panels      -> 3D
"""
import numpy as np
import pandas as pd

array = np.arange(10, 21)
print(array)

data = {'srno': 1, 'roll': '22AB123', 'name': 'Jennie'}

# series = pd.Series(array)
series = pd.Series(data)
print(series)
print("~~~~~~~")
print(series[1:3])

# DataFrame
numbers = [10, 20, 30, 40, 50]
data = [{'roll': 101, 'name': 'John', 'age': 20}, {'roll': 201, 'name': 'Fionna', 'age': 21, 'email': 'fionna@example.com'}]

# table = pd.DataFrame(numbers)
# table = pd.DataFrame(data)
table = pd.DataFrame(data, index=['first', 'second'])
print(table)

data = {
    'one': pd.Series([11, 22, 33], index=['a', 'b', 'c']),
    'two': pd.Series([44, 55, 66, 77], index=['a', 'b', 'c', 'd']),
}

print(data['one'])

table = pd.DataFrame(data)
print(table)

table['three'] = pd.Series([99, 77, 88], index=['a', 'b', 'c'])
print(table)

# del table['one']
# table.pop('three')
# print(table)

print(table.loc['c'])
print(table.iloc[2])

new_table = table.drop('a')
print(table)
print(new_table)

table = pd.read_csv('products.csv')
print(table)

table.to_csv('new-products.csv')

# sheet_table = pd.read_excel('somefile.xlsx')
# sheet_table.to_excel('anyfile.xlsx')
