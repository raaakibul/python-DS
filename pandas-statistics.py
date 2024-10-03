import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'name':['Ana', 'Bob', 'John', 'Mike'],
    'Age':[24,26,28,29],
    'height':[176,165,187,182],
    'gender':['f','m','m','m']
}

df = pd.DataFrame(data)
print(df.count())
print(df['Age'].count())
print(df['height'].mean())
print(df['height'].mode())
print(df['height'].median())
print(df['height'].std())
print(df.describe())