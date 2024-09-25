import numpy as np 

a = np.array([1,2])
print(a)

# multi dimensional arrays

b = np.array([
    [1,2,3,4],
    [1,3,5,6]
])
print(b)

print(a.ndim)
print(b.ndim)
print(b.shape)

print(a.size)