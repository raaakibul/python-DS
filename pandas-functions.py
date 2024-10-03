import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
data = {
    'name':['Ana', 'Bob', 'John', 'Mike'],
    'Age':[24,26,28,29],
    'height':[176,165,187,182],
    'gender':['f','m','m','m']
}

df = pd.DataFrame(data)
print(df['height'].apply(np.sin))
print(df['height'].apply(lambda x: x*100))