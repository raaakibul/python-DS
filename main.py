import numpy as np 

a = np.array([1,2,3,4,5])
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

# Elements and indexing 
print(a)
print(a[2])

# Advanced indexing
z = a[[0,2,4]]
print(z)

# initialization zeros
x = np.ones((3,3))
print(x)

y = np.full((2,2),99, dtype='int32')
z = np.full_like(x,12)
print(z)