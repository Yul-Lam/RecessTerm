#They are inbuilt

#np.array() function
import numpy as np
array1= np.array([8, 2, 5])
print(array1)

#np.zeros() - creates an array filled with zeros

zeros_array = np.zeros((4, 5)) 
print(zeros_array)


#random function

random_array = np.random.rand(4, 5)
print(random_array)

#Mathematical and statistical Functions

arrays = np.array([30, 50, 10])
total = np.sum(arrays)
print(total)