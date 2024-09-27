import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')
style.use('fivethirtyeight')
x = np.arange(0,30,0.2)
y =np.sin(x)

plt.plot(x, y)
plt.show()