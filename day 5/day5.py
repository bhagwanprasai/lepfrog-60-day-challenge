#basics of numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

#0d array

import numpy as np

arr = np.array(42)

print(arr)


#1d array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#2darray

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

#3d array
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


#checking dimension

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#higher power array
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

#slicing aaray

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

#-ve slicing
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])


#step 
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

#slicing 2d array
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])