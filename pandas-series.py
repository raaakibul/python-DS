import pandas as pd 
import matplotlib.pyplot as plt

series = pd.Series([10,20,30,40], ['A','B','C','D'])

print(series)

# print(series.iloc[1])

series.plot()

plt.show()