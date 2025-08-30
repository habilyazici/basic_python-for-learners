import pandas as pd

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","abc"]
}

df = pd.DataFrame(data)
print(df)
print("\n" + 20 * '-' + "\n")

def kareal(x):
    return x * x
kareal2 = lambda x: x * x

print('Column2 unique values:', df["Column2"].unique())
print('Column2 unique count:', df["Column2"].nunique())
print('Column2 value counts:', df["Column2"].value_counts())
print("\n" + 20 * '-' + "\n")

print('Column3 * 2:\n', df["Column3"] * 2)
print("\n" + 20 * '-' + "\n")
print('Column1 kareal:\n', df["Column1"].apply(kareal))
print("\n" + 20 * '-' + "\n")
print('Column1 lambda kare:\n', df["Column1"].apply(lambda x: x * x))
print("\n" + 20 * '-' + "\n")

df["Column4"] = df["Column3"].apply(len)
df.columns = ["col1", "col2", "col3", "col4"]
print('Column names:', df.columns)
print('Column count:', len(df.columns))
print('Index info:', df.index)
print('Index count:', len(df.index))
print("\n" + 20 * '-' + "\n")

print('DataFrame info:', df.info())
print("\n" + 20 * '-' + "\n")
print('DataFrame dtypes:\n', df.dtypes)
print("\n" + 20 * '-' + "\n")
print('DataFrame describe:\n', df.describe())
print("\n" + 20 * '-' + "\n")
print('DataFrame ndim:  ', df.ndim)
print('DataFrame shape:\n', df.shape)
print('DataFrame size:\n', df.size)
print("\n" + 20 * '-' + "\n")

print('df sıralama normal:\n', df.sort_values("col2"))
print("\n" + 20 * '-' + "\n")
print('df sıralama tersten:\n', df.sort_values("col3", ascending = False))
print("\n" + 20 * '-' + "\n")