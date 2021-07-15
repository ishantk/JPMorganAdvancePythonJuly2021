"""
    Data Analysis
    We work on data to give insights to help take decisions in business

    Steps:
        > Transform the raw data into some desired format
        > pre processing of data
        > Prepration of Models
        > Analyse trends and make decisions
"""
# Numpy -> Numerical Python -> We can do scientific computing
# pip install numpy
# Multi Dimensional Array

import numpy as np
numbers = [10, 20, 30, 40, 50]
array = np.array([10, 20, 30, 40, 50])

print(numbers)
print(array, type(array))

multi_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multi_dim_array)

array1 = np.arange(10, 100)
print(array1)

array2 = np.ones((8, 8)) #np.zeros((8, 8))
print(array2)

vector = np.linspace(0, 20, 6)
print(vector)

array3 = np.zeros(8)
print(array3)
array4 = array3.reshape((2, 2, 2))
print(array4)

array5 = array4.ravel()
print(array5)

array6 = np.arange(1, 21)
print(len(array6))
array_slice = slice(1, 10, 2)
print(array6[3:10])
print(array6[array_slice])

array7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array7[0:2, 0:2])

print(array7.shape)
print(array7.ndim)
print(array7.itemsize)

array8 = np.empty((3, 3), dtype=int)
print(array8)

array_from_text = np.loadtxt("data.txt")
print(array_from_text)
np.savetxt("new-data.txt", array_from_text)
print("Data Saved")

array_from_csv = np.genfromtxt('some-data.csv', delimiter=",")
# np.savetxt('some-data.csv', array_from_text, delimiter=",")
print(array_from_csv)
