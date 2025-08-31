import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])
df = df.reindex(['a','b','c','d','e','f','g','h'])
print(df)
print("\n" + 20 * '-' + "\n")

df["column4"] = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
print(df)
print("\n" + 20 * '-' + "\n")

print('column silme:\n', df.drop("column1", axis = 1))
print("\n" + 20 * '-' + "\n")
print('çoklu column silme:\n', df.drop(["column1","column2"], axis = 1))
# satır ile de yapılabiliyor
print("\n" + 20 * '-' + "\n")

print('Boş veriler null:\n', df.isnull()) # notnull() tam tersi
print("\n" + 20 * '-' + "\n")
print('her sütun null sayısı:\n', df.isnull().sum())
print('her sütun null sayısı:\n', df.isnull().sum().sum())
print("\n" + 20 * '-' + "\n")
print('column1 null:\n', df["column1"].isnull())
print("\n" + 20 * '-' + "\n")
print('column1 dolu değerler:\n', df[df["column1"].notnull()])
print("\n" + 20 * '-' + "\n")
print('column1 dolu değerler ile tüm veriler:\n', df[df["column1"].notnull()]["column1"])
print("\n" + 20 * '-' + "\n")
print('tüm dolu veriler:\n', df[df.notnull().all(axis=1)])
print("\n" + 20 * '-' + "\n")

print('herhangi null içeren satırı sil:\n', df.dropna())
# otomatik olarak axis = 0 parametresi ise how= "any" dir
print("\n" + 20 * '-' + "\n")
print('hepsi null satır sil:\n', df.dropna(how = "all"))
print("\n" + 20 * '-' + "\n")
print('herhangi null içeren sütunu sil:\n', df.dropna(axis = 1))
print("\n" + 20 * '-' + "\n")

print('col1 ve col3 de herhangi null verinin satırı sil:\n', df.dropna(subset = ["column1","column3"], how = "any"))
print("\n" + 20 * '-' + "\n")
print('col1 ve col3 de tüm null verinin satırı sil:\n', df.dropna(subset = ["column1","column3"], how = "all"))
print("\n" + 20 * '-' + "\n")
print('bir satırda en az 2 dolu veri olmalı:\n', df.dropna(thresh = 2))
print("\n" + 20 * '-' + "\n")

print('NaN yerine yazılır:\n', df.fillna(value = 'no input'))
print("\n" + 20 * '-' + "\n")
print('NaN yerine 1:\n', df.fillna(value = 1))
print("\n" + 20 * '-' + "\n")

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

print("Boş verileri tüm ortalamalarla doldur:\n", df.fillna(value = ortalama(df)))

print("\n" + 20 * '-' + "\n")
print(df.mean())
print(df.fillna(df.mean(), axis = 0))