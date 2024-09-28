import matplotlib.pyplot as plt
import numpy as np

nationalities = ['American','German','Spanish','Other']
students = [60,23,21,34]

explode = [0,0,0.1,0]

plt.pie(students, labels= nationalities, autopct='%.2f%%', explode=explode)
plt.show()