import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')
# style.use('fivethirtyeight')
# style.use('dark_background')
# style.use('grayscale')
x = np.arange(0,30,0.2)
y1 =np.sin(x)
y2 =np.cos(x)
# plt.grid(True)
plt.title('Sine function')
# plt.suptitle('I am bigger')


plt.plot(x, y1, label='sine')
plt.plot(x, y2, label='cosine')
plt.legend(loc='upper left')
plt.show()