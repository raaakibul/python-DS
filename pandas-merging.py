import pandas as pd 

data = {
    'SSN':[2,5,7,8],
    'name':['Ana', 'Bob', 'John', 'Mike'],
    'Age':[24,26,28,29]
}

data2 = {
    'SSN':[1,2,3,4],
    'height':[176,165,187,182],
    'gender':['f','m','m','m']
}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

df = pd.merge(df1,df2, on='SSN', how='outer')
df.set_index('SSN',inplace=True)
print(df)