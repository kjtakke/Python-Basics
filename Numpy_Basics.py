# https://www.w3schools.com/python/numpy_creating_arrays.asp

import numpy as np

#1D Array
arr = np.array([1, 2, 3, 4, 5])
#print(arr)


#2D Array
arr = np.array([[1, 2, 3], [4, 5, 6]])
#print(arr)

#3D Array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#print(arr)

#Check dimentions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)


#Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[1:5])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[4:])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[:4])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[-3:-1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#print(arr[1, 1:4])




#Stepping
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[::2])



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#print(arr[0:2, 1:4])


#From Numpy to Pandas to Numpy
import pandas as pd

df =[[21, 72, 67], [23, 78, 69], [32, 74, 56], [52, 54, 76]]
#print(df)

df = pd.DataFrame(df, columns=['a', 'b', 'c'])
#print( df)

arr = df.to_numpy()
#print(arr)

#random
from numpy import random

x = random.randint(100, size=(3))
#print(x)

x = random.randint(100, size=(3, 5))
#print(x)


x = random.rand(5)
#print(x)

x = random.rand(5, 5)
#print(x)

x = random.choice([3, 5, 7, 9])
#print(x)

#For a full list of numpy function
#help(np)

