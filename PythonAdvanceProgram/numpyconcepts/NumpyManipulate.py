import numpy as np
from numpy.ma.core import reshape

#reshape

a = np.arange(1,7)
print("Original",a)
reshaped = a.reshape(2,3)
print(reshaped)

#flat -- returns 1d iterator over the array

arr = np.array([1,2],int)
for x in arr.flat:
    print(x)

#flatten - return a copy of the array collapsed into 1 dimension

arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

# ravel() - retuns a flattened array

arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

#pad() - returns a padded array with shape increased according to padwidth
arr = np.array([1,2,3])
padded = np.pad(arr, 3,mode = 'constant')
print(padded)

# Transpose operations
''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)



#joining arrays -- concatenate

a= np.array([[1,2],[3,4]])
b= np.array([[5,6],[8,9]])

print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

#stack - join the arrays along the new axis
# Adds a new dimension
# All arrays must have the same shape

a= np.array([1,2,4])
b= np.array([5,6,9])

print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=0))

# hstack -- Stacks arrays horizontally(column wise)

a= np.array([[1,2],[3,4]])
b= np.array([[5,6],[8,9]])
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis = 1))

#vstack() -- Stack arrays Vertically(row-wise)
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis = 0))

#column_stack() - Stacks 1D arrays as columns into 2D array
a= np.array([1,2,4])
b= np.array([5,6,9])
print(np.column_stack((a,b)))

#row_stack() -- Stacks arrays row-wise
print(np.vstack((a,b)))


# Splitting Arrays

# split arrays into multiple sub-arrays based on axis
arr = np.array([1,2,3,4,5,6])

res = np.split(arr,3)
print(res)

#hsplit() - Splits array horizontally (column-wise)

# works for 2D array

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(arr2,2))

#vsplit Splits array Vertically (row - wise)
arr3 = (np.array([[1,2],[3,4],[5,6],[7,8]]))
print(np.vsplit(arr3, 2))

# array split - similar to split but does not require equal division

arr = np.array([1,2,3,4,5])
print(np.array_split(arr,3))
#Adding/removing elements
#resize() -- Returns a new array with a specified shape

arr = np.array([1,2,3,4,8,5])
new_arr = np.reshape(arr,(2,3))
print(new_arr)

#2D array
a= np.array([[1,2],[3,4]])
b= np.array([[5,6]])

print(np.append(a,b,axis = 0))

# Insert values before given index
arr=np.array([10,20,30])
new_arr = np.insert(arr,2,15)
print(new_arr)

#deletes elements along a specified axis
arr=np.array([10,20,30])
new_arr = np.delete(arr,2)
print(new_arr)

#unique()
arr = np.array([1,2,2,3,4,4,5])
print(np.unique(arr))

#Repeating
# repeat() is used to repeat each element of an array a specified number of times
#each element is repeated twice
arr = np.array([10,20,30])
print(np.repeat(arr,[1,2,3]))

# Repeat in 2 elements
arr2 = np.array([[1,2],[3,4]])
print(np.repeat(arr2,2,axis=0))

#tile() the input array that will be repeated

arr = np.array([1,2,3])
tiled_arr = np.tile(arr,2)
print("Original array",arr)
print("Tiled array",tiled_arr)

#Rearranging elements
#flip -- reverse the order
#if axis = None - rev entire flattened array
#if axis = 1 - rev the row
#if axis = 2 - rev the column

arr = np.array([1,2,3,4])
print(np.flip(arr))

#2D
arr2 = np.array([[1,2],[3,4]])
print(np.flip(arr2,axis=0))#flip rows
print(np.flip(arr2,axis=1))#flip columns

#flipr() - flip left-Right (axis=1) - Works only on 2D+ arrays
arr2 = np.array([[1,2,8],[3,4,9]])
print(np.fliplr(arr2))

#flipud - Flip up down (axis=0)
print(np.flipud(arr2))

#roll() - Rolls (rotates) elements along a given axis
arr2 = np.array([[1,2,3],[4,5,8]])
print(np.roll(arr2,2,axis=None))

#Sorting and Searching

#sort() - Returns a sorted copy of an array (or sorts in place if using ndarray method)
arr = np.array([5,2,9,3])
sort = np.sort(arr)
print(sort)


#args sort -- returns the indices that would sort the arr returns the index position
arr = np.array([5,2,9,3])
ind = np.argsort(arr)
print(ind)

#lexsort() -- Used for sorting with multiple columns
#Sort by a first
#Then by b(secondary key)

a=np.array([1,1,0,0])
b=np.array([1,0,1,0])
res = np.lexsort((b,a))
print(res)



#Changing dimensions


