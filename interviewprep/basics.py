import numpy as np #numerical python, arrays (50x faster than lists as arrays are stored at one continuous place in memory unlike lists, written in c, c++, python)

print(np.__version__)
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr[2] + arr[3])

# 0-D arrays
for x in arr:
  print(x)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('Last element from 2nd dim: ', arr[1, -1])  # Use negative indexing to access an array from the end.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Slicing arrays
print(arr[1:5]) # index 1 to 5
print(arr[4:]) # index 4 to end
print(arr[:4]) # index 0 to 4
print(arr[-3:-1]) # Slice from the index 3 from the end to index 1 from the end
print(arr[1:5:2]) # Return every other element from index 1 to index 5:
print(arr[::2]) # Return every other element from the entire array:

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #From the second element, slice elements from index 1 to index 4 (not included)
print(arr[0:2, 2]) #From both elements, return index 2
print(arr[0:2, 1:4]) #From both elements, slice index 1 to index 4 (not included), this will return a 2-D array.

#data type conversions - https://www.w3schools.com/python/numpy/numpy_data_types.asp
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

#copy and view - https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

x = arr.view()
arr[0] = 42
print(arr)
print(x)

x[0] = 31
print(arr)
print(x)

x = arr.copy()
y = arr.view()
print(x.base) #The copy returns None. Copies owns the data, and views does not own the data, but how can we check this
print(y.base) # returns the original array, so y is a view


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

#reshape array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # returned array is a copy or a view

#Iterating arrays - https://www.w3schools.com/python/numpy/numpy_array_iterating.asp
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)
# instead use nditer() helper function that can be used to iterate through the arrays
for x in np.nditer(arr):
  print(x)

#Joining arrays - https://www.w3schools.com/python/numpy/numpy_array_join.asp
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1) #Join two 2-D arrays along rows (axis=1):
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1) #Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
print(arr)

arr = np.hstack((arr1, arr2)) #helper function: hstack() to stack along rows
print(arr)

arr = np.vstack((arr1, arr2)) #helper function: vstack() to stack along columns
print(arr)

arr = np.dstack((arr1, arr2)) #helper function: dstack() to stack along height, which is the same as depth.
print(arr)

#Splitting arrays - https://www.w3schools.com/python/numpy/numpy_array_split.asp
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

newarr = np.array_split(arr, 4)
print(newarr)

newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

#Searching arrays - https://www.w3schools.com/python/numpy/numpy_array_search.asp
arr = np.array([1, 2, 3, 4, 5, 4, 4]) #Find the indexes where the value is 4: 
x = np.where(arr == 4) 
print(x)

x = np.where(arr%2 == 0)
print(x)

x = np.where(arr%2 == 1)
print(x)

x = np.searchsorted(arr, 5) #Find the indexes where the value 5 should be inserted:
print(x)

#Sorting arrays - https://www.w3schools.com/python/numpy/numpy_array_sort.asp
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))


#Filtering arrays - https://www.w3schools.com/python/numpy/numpy_array_filter.asp
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)