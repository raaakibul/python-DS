import pandas as pd 

data = {
    'name':['Ana', 'Bob', 'John', 'Mike'],
    'Age':[24,26,28,29]
}

data2 = {
    'height':[176,165,187,182],
    'gender':['f','m','m','m']
}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

df = pd.merge(df1,df2)