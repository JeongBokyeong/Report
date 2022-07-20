from scipy.stats import pearsonr
import numpy as np
import pandas as pd

df = pd.read_excel ('dataframe.xlsx')   
df.head()
x = df.iloc[:,1] 
y = df.iloc[:,5] #수도권 과밀화율

# print(pearsonr(x, y))

print(pearsonr(x, y)[0])