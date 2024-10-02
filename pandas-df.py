import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'name':['Ana', 'Bob', 'John', 'Mike'],
    'Age':[24,26,28,29],
    'height':[176,165,187,182],
    'gender':['f','m','m','m']
}

df = pd.DataFrame(data)
print(df)
print(df.size)
print(df.dtypes)
print(df.T)

print(df['name'].iloc[1])