import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')
# style.use('fivethirtyeight')
# style.use('dark_background')
style.use('grayscale')
x = np.arange(0,30,0.2)
y =np.sin(x)

# plt.grid(True)
plt.title('Sine function')
# plt.suptitle('I am bigger')


plt.plot(x, y)
plt.show()