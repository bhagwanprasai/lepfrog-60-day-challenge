#start of ml journey
#mean median mode standard deviation
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)
m  = np.std(speed)
n = np.var(speed)
print(x)
print(y)
print(z)
print(m)
print(n)

#percentile
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = np.percentile(ages, 75)
print(x)

#data distribution
x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

x = np.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

#scatter plot
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()