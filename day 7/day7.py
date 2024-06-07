#numpy ufunc
#concept of vectorization using numpy
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

#same can be acieved  using this
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


#universal function using numpy

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add))

#arithmetic operations
#using add to add array and store the value in new array

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)
#sub

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

#product


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

#divide

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.divide(arr1, arr2)

print(newarr)
#power remainder quotient mod absoulte value 
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([3, 2, 3, 4, 3, 5])
arr = np.array([-1, -2,-3,-4,-5])
newarr = np.power(arr1, arr2)
newarr2 = np.remainder(arr1,arr2)
newarr3 = np.divmod(arr1,arr2)
newarr4 = np.absolute(arr)
print(newarr)
print(newarr2)
print(newarr3)
print(newarr4)

#managing decimal values
arr = np.trunc([-3.1666, 3.6667])
arr1 = np.fix([-3.1666, 3.6667])
arr2 = np.around(3.1666, 2)
arr3 = np.floor([-3.1666, 3.6667])

print(arr)
print(arr1)
print(arr2)
print(arr3)

#log
arr = np.arange(1, 10)

print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))

#summation
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)
arr = np.array([1, 2, 3])

newarr1 = np.cumsum(arr)

print(newarr)

print(newarr1)

#lcm
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

#gcd
num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)