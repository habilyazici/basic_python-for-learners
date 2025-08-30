import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["diyabet","şeker","insulin"])
print(df)

print("diyabet sutunu:\n", df["diyabet"])
print("diyabet type: ", type(df["diyabet"]))
print("\n" + 20 * '-' + "\n")
print("diyabet-şeker sutunu:\n", df[["diyabet","şeker"]])
print("\n" + 20 * '-' + "\n")

print('A satırı:\n', df.loc["A"])
print("\n" + 20 * '-' + "\n")
print('A satırı, diyabet sutunu:', df.loc["A", "diyabet"])
print('Tüm satırlar, diyabet sutunu:\n', df.loc[:, "diyabet"])
print("\n" + 20 * '-' + "\n")
print('A-B satırı, şeker sonrası:\n', df.loc["A":"B", "şeker":])
print("\n" + 20 * '-' + "\n")
print('A ve B satırı, diyabet ve şeker sutunu:\n', df.loc[["A","B"],["diyabet","şeker"]])
print("\n" + 20 * '-' + "\n")
print(df[df["insulin"] > 0])
print(df.loc[df["insulin"] > 0])
print("\n" + 20 * '-' + "\n")

print("2. satır:\n", df.iloc[2])
print('2. satır, şeker sutunu:\n', df.iloc[2, 1])
print("\n" + 20 * '-' + "\n")
print('Tüm satırlar, diyabet ve şeker sutunu:\n', df.iloc[:, [0, 1]])
print("\n" + 20 * '-' + "\n")
print('0 ve 1 satırları, tüm sutunlar:\n', df.iloc[[0, 1], :])
print("\n" + 20 * '-' + "\n")
print('0-1 satırları, diyabet-şeker sutunu:\n', df.iloc[0:1, 0:2])
print("\n" + 20 * '-' + "\n")

df["kan"] = pd.Series(randn(3), ["A","B","C"])
df["column5"] = df["diyabet"] + df["kan"]

df.drop("column5", axis = 1, inplace = True)
print(df)