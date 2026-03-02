# types of arrays -- 1D, 2C, 3D

import numpy as np
from numpy.ma.core import identity

#1D array
a = np.array([1,2,3])
print(a)
#2D array
b = np.array([[1,2],[3,4]])
print(b)
#1D array
a = np.array([[1,2],[4,7],[2,2]])
print(a)

#create a array with specific data type -- complex
a = np.array([1,2,3], dtype=complex)
print(a)

#create a array with specific data type-- float
a = np.array([1,2,3], dtype=float)
print(a)

#create a array with specific data type-- int
a = np.array([1,2,3], dtype=int)
print(a)


#arrange func

'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''

a=np.zeros(5)
print(a)
# 2d array zeros
a_2D=np.zeros(5)
print(a_2D)

#using numpy.ones fun
a = np.ones(5)
print(a)
# 2d array zeros
a_2D=np.ones(4,int)
print(a_2D)



# using numpy.arrange() fun
# the numpy.arrange fun creates an array by generating a seq of num based on space

# providing the start, stop and step values
a= np.arange(1,10,2)
print(a)

#using numpy.linspace() function
#linspace() is used to generate evenly spaced num over a specified interval
# end point is true last no is included

a = np.linspace(0,5,endpoint=True)
print(a)

#exclude the last num
a = np.linspace(0,5,endpoint=False)
print(a)

#using numpy.random.rand() fun
# generates an array of the specifies shape with random values
# if no argument is provided it returns single float value

a=np.random.rand(5)
print(a)
#2D
a=np.random.rand(2,3)
print(a)
#3D
a=np.random.rand(2,3,4)
print(a)

# using numpy.empty() Function
#2D
#This fun initialises an array without initialising its element
#The content of the array ia arbitary and may vary
a = np.empty((2,3))
print(a)

#using numpy.full() Function
#In the following ex we are using the numpy.full fun to create a 2D array
# filled entirely with the value 5

a = np.full((2,3),5)
print(a)


#numpy.eye() -- 2D array with 1s i diag and zero remaining

identity_matrix = np.eye((4))
print(identity_matrix)
#numpy.identity -- generate square identity matrix
identity_matrix = np.eye((5))
print(identity_matrix)
#numpy.diag -- creates a square diagnol matrix with the elements and the diagnol values and zeroes in the remaining values

Matrix = np.array([[10,20,30],[11,12,13],[15,18,19]])
print("Original matrx",Matrix)
dig_elements= np.diag(Matrix)
print("diagonal Matrix",dig_elements)



