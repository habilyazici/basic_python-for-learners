import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
# numpy nesnesiyle oluşturulmuş 15*5'lik matris

df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])
print(df)
print("\n" + 20 * '-' + "\n")

print("df columns: ", df.columns)
print('ilk 5 satır:\n', df.head())
print("\n" + 20 * '-' + "\n")
print('son 5 satır:\n', df.tail())
print("\n" + 20 * '-' + "\n")
print('karışık 5 satır:\n', df.sample(5))
print("\n" + 20 * '-' + "\n")

print('Column1 ilk 3:\n', df["Column1"].head(3))
print("\n" + 20 * '-' + "\n")
print('Col1-Col2 son 3:\n', df[["Column1","Column2"]].tail(3))
print("\n" + 20 * '-' + "\n")
print('5-15 arası Col1-Col2 son 3:\n', df[5:15][["Column1","Column2"]].sample(3))
print("\n" + 20 * '-' + "\n")

print('df>50 değerler:\n', df[df >= 50])
print("\n" + 20 * '-' + "\n")
print('Col1 50-70:\n', df[(df["Column1"] > 50) & (df["Column1"] <= 70)])
print("\n" + 20 * '-' + "\n")
print('Col1>50 Col1-Col2:\n', df[ df["Column1"] > 50 ][["Column1","Column2"]])
print("\n" + 20 * '-' + "\n")

print('Col1>50 Col2<=70:\n', df[(df["Column1"] > 50) & (df["Column2"] <= 70)])
print('Col1>50 veya Col2>50:\n', df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]])
print('query & çift:\n', df.query("Column1 >= 50 & Column1 % 2 == 0"))
print('query & çift Col1-Col2:\n', df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]])
print('query | çift Col1-Col2:\n', df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]])
