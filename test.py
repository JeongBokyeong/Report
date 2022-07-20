# from tkinter import Y
from statistics import mode
from tkinter import X
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv ('data.csv', encoding='cp949')   
df.head()
X = df.iloc[:,1] #신생아 출산인구
y = df.iloc[:,5] #수도권 과밀화율

# plt.plot(X, y, 'o')
# plt.show()

model = LinearRegression()
model.fit(X.values.reshape(-1,1),y)

#print(model.predict([[3.7]]))

# print(X.shape, y.shape)

# for i in range(len(X)):
#     y[i] = X[i]
    # print(X.values)
    #X[i] = model.predict(X[i].values.reshape(-1,1))

# print(model.predict([[44]]))

# plt.plot(X, y, 'o')
plt.plot(y, X, 'o')

# plt.plot(X, model.predict(X.values.reshape(-1,1)))    
plt.plot(model.predict(X.values.reshape(-1,1)), X, )
plt.show()
