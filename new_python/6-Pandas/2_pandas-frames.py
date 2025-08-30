import pandas as pd

list = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
dictt = {"Name": ["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade": [50, 60, 70, 80]}
dict_list = [
                {"Name": "Ahmet", "Grade": 50},
                {"Name": "Ali", "Grade": 60},
                {"Name": "Yağmur", "Grade": 70},
                {"Name": "Çınar", "Grade": 80}
            ]

print("boş dataframe:\n", pd.DataFrame())
print("boş dataframe tipi:\n", type(pd.DataFrame()))
print("\n" + 20 * '-' + "\n")
# hepsinin boyutu 2'dir, shapeleri farklıdır
print("4 satır 1 sütun:\n", pd.DataFrame([10,20,30,40]))
print("\n" + 20 * '-' + "\n")
print("1 satır 4 sütun:\n", pd.DataFrame([[10,20,30,40]]))
print("\n" + 20 * '-' + "\n")
print("2 satır 4 sütun:\n", pd.DataFrame([[10,20,30,40], [50,60,70,80]]))
print("\n" + 20 * '-' + "\n")
print("list:\n", pd.DataFrame(list))
print("\n" + 20 * '-' + "\n")
print("list dataframe:\n", pd.DataFrame(list, index = ['a','b','c','d'], columns = ['Name','Grade']))
print("\n" + 20 * '-' + "\n")
print("dictt dataframe:\n", pd.DataFrame(dictt))
print("\n" + 20 * '-' + "\n")
print("dict dataframe2:\n", pd.DataFrame(dictt, index = ["212","232","236","456"]))
print("\n" + 20 * '-' + "\n")
print("dict_list dataframe:\n", pd.DataFrame(dict_list))
print("\n" + 20 * '-' + "\n")
print("dict_list dataframe2:\n", pd.DataFrame(dict_list, index=["212","232","236","456"]))
print("\n" + 20 * '-' + "\n")

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])
print("serilerin birleşimi list:\n", pd.DataFrame([s1,s2]))
print("\n" + 20 * '-' + "\n")
print("serilerin birleşimi:\n", pd.DataFrame({'s1 column': s1, 's2 column': s2}))
print("\n" + 20 * '-' + "\n")