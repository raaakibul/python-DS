import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100,0.2)

y1 = np.sin(x)
y2 = x ** 2 + 2 * x

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)

ax1.plot(x,y1)
ax2.plot(x,y2)

plt.show()