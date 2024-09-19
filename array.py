import numpy as np 
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(a[0])
print(b[1])

c = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

print(c.shape)

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

print(x+y)

# fill arrays
# np.full()
# np.ones()
# np.empty()
zero_array = np.zeros((5,7,3))
print(zero_array)

# range functions
f = np.array([0,5,10,15,20])
f1 = f *2 - f**2

print(f1)