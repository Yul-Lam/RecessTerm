#Numpy arrays support various mathematical operations. this can be achieved on individual elements
import numpy as np

w = np.array([[3, 7], [5, 10]])

p=np.array([[5.1, 2.3], [6.1, 1]])

print("Adding 2 to every element: \n", w + 2)
print ("Subtracting 1 from every element: \n", w - 1)

#Array sum

print("Array sum: \n", w + p)

#sum of all array elements

print("Sum of all array elements: ", w.sum())