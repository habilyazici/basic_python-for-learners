import pandas as pd

list = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
dictt = {"Name": ["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade": [50, 60, 70, 80]}
dict_list = [
                {"Name": "Ahmet", "Grade": 50},
                {"Name": "Ali", "Grade": 60},
                {"Name": "Yağmur", "Grade": 70},
                {"Name": "Çınar", "Grade": 80}
            ]

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])
data = dict(apples = s1 , oranges = s2)
print(pd.DataFrame(data))
print("\n" + 20 * '-' + "\n")

df = pd.DataFrame()
print("boş dataframe:\n", df)
print(type(df))
print("\n" + 20 * '-' + "\n")
print("normal dataframe:\n", pd.DataFrame([1,2,3,4]))
print("\n" + 20 * '-' + "\n")
print("list dataframe:\n", pd.DataFrame(list, index = ['a','b','c','d'], columns = ['Name','Grade']))
print("\n" + 20 * '-' + "\n")
print("dict dataframe:\n", pd.DataFrame(dictt))
print("\n" + 20 * '-' + "\n")
print("dict dataframe2:\n", pd.DataFrame(dictt, index = ["212","232","236","456"]))
print("\n" + 20 * '-' + "\n")
print("dict_list dataframe:\n", pd.DataFrame(dict_list))
print("\n" + 20 * '-' + "\n")
print("dict_list dataframe2:\n", pd.DataFrame(dict_list, index = ["212","232","236","456"]))