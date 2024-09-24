import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(-100,100,1)
y = 0.5 * x**2 + 2 * x

plt.plot(x,y)
plt.show()