import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_excel('dataframe.xlsx')
df = df.iloc[:,0:1]
"""
df = df.transpose()    #행 열 전환
df.rename(columns=df.iloc[0], inplace=True)    # 행열이 전환된 데이터프레임의 열 이름 제대로 수정
df = df.drop(df.index[0])
"""
print(df)

sns.heatmap(df)
plt.show()     

sns.heatmap(df, cmap='viridis')
plt.show()     

sns.heatmap(df, annot=True) #숫자 출력
plt.show()   