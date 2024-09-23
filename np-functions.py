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
# 1 dimensional array
print(a.flatten())

print(a.flat[7])

b = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [70,80,10,20]
    
])

c = np.concatenate((a,b))
c2 =np.stack((a,b))
print(c)

print(c2)