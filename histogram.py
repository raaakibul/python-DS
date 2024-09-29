import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 172, 8
x = mu +  sigma * np.random.randn(10000)

plt.hist(x,100, facecolor='blue', density=True)
plt.show()