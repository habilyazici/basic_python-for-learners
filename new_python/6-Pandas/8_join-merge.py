import pandas as pd

customers = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7],
    'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

print("df_customers:\n", df_customers)
print("\n" + 20 * '-' + "\n")
print("df_orders:\n", df_orders)
print("\n" + 20 * '-' + "\n")

# Merge ile iki dfyi birleştirmek için ortak bir sutunları olması gerekir.
# on="CustomerId", left_on="a_column" ve right_on="b_column" ile ortak sutunları belirtebiliriz.
result1 = pd.merge(df_customers, df_orders, how="inner")
result2 = pd.merge(df_customers, df_orders, how="left")
result3 = pd.merge(df_customers, df_orders, how="right")
result4 = pd.merge(df_customers, df_orders, how="outer")

print("iki df inner join:\n", result1)
print("\n" + 20 * '-' + "\n")
print("iki df left join:\n", result2)
print("\n" + 20 * '-' + "\n")
print("iki df right join:\n", result3)
print("\n" + 20 * '-' + "\n")
print("iki df outer join:\n", result4)
print("\n" + 20 * '-' + "\n")

data1 = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

data2 = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

df_data1 = pd.DataFrame(data1)
df_data2 = pd.DataFrame(data2)

print("df_data1:\n", df_data1)
print("\n" + 20 * '-' + "\n")
print("df_data2:\n", df_data2)
print("\n" + 20 * '-' + "\n")

result1 = pd.concat([df_data1, df_data2])
result2 = pd.concat([df_data1, df_data2], axis=1)

print("concat axis 0:\n", result1)
print("concat axis 1:\n", result2)
print("\n" + 20 * '-' + "\n")

df1 = pd.DataFrame({'A': [1, 2], 'B': [5, 6]}, index=['x', 'y'])
df2 = pd.DataFrame({'D': [3, 4], 'E': [9, 10]}, index=['x', 'y'])

print("join ile iki df birleştirme:\n", df1.join(df2))
print("\n" + 20 * '-' + "\n")

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}
df = pd.DataFrame(data)
print(df)
print("\n" + 20 * '-' + "\n")

print(df.pivot_table(index="Ay", columns= "Kategori", values= "Gelir"))