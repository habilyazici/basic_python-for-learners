import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])
print(df)

print("Column1:\n", df["Column1"])
print("Column1 type: ", type(df["Column1"]))
print("\n" + 20 * '-' + "\n")
print("Column1-Column2:\n", df[["Column1","Column2"]])
print("\n" + 20 * '-' + "\n")

print('A,Column1:', df.loc["A", "Column1"])
print("\n" + 20 * '-' + "\n")
print('A satırı:\n', df.loc["A"])
print('type(df.loc["A"]):', type(df.loc["A"]))
print("\n" + 20 * '-' + "\n")
print('Tüm satırlar Column1:\n', df.loc[:, "Column1"])
print("\n" + 20 * '-' + "\n")

print('df.iloc[2]:\n', df.iloc[2])
print('df.loc[:,["Column1","Column2"]]:\n', df.loc[:,["Column1","Column2"]])
print("\n" + 20 * '-' + "\n")
print('Col1-Col3 dilim:\n', df.loc[:,"Column1":"Column3"])
print("\n" + 20 * '-' + "\n")
print('Başlangıç-Col2:', df.loc[:,:"Column2"])
print("\n" + 20 * '-' + "\n")

print('A-B satırları, Col2ye kadar:\n', df.loc["A":"B", :"Column2"])
print("\n" + 20 * '-' + "\n")
print('Başlangıç-B satırları, Col2ye kadar:\n', df.loc[:"B", :"Column2"])
print("\n" + 20 * '-' + "\n")
print('A satırı, Col2:\n', df.loc["A", "Column2"])
print("\n" + 20 * '-' + "\n")
print('A-B satırları, Col1-Col2:\n', df.loc[["A","B"],["Column1","Column2"]])
print("\n" + 20 * '-' + "\n")

df["Column4"] = pd.Series(randn(3), ["A","B","C"])
df["Column5"] = df["Column1"] + df["Column3"]

df.drop("Column5", axis = 1, inplace = True)
print(df)