import numpy as np 

a = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]
])

print(np.sin(a))
print(np.cos(a))
print(np.median(a))

print(np.size(a))

a = a.reshape((2,6))
print(a)
print(a.flatten())
