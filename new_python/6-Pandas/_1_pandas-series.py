import pandas as pd
import numpy as np
import sqlite3

# df = pd.read_csv('datasets/sample.csv')
# df = pd.read_excel("datasets/sample.xlsx")
# df = pd.read_json('datasets/sample.json', encoding="UTF-8")
# connection = sqlite3.connect("datasets/sample.db")
# df = pd.read_sql_query("SELECT * FROM students", connection)

numbers = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']
dict = {'a': 30, 'b': 40, 'c': 50, 'd': 60}
random_numbers = np.random.randint(10, 100, 6)

print("boş seri:\n ",pd.Series())
print("boş seri:\n ",type(pd.Series()))
print("\n" + 20 * '-' + "\n")

print("Numbers:\n",pd.Series(numbers))
print("Letters:\n",pd.Series(letters))
print("Dictionary:\n",pd.Series(dict))
# index belirlenirse dictin keyi ezilir. Series ve frames dict veya list alır

print("\n" + 20 * '-' + "\n")
print("Random Numbers:\n", pd.Series(random_numbers))
print("Numbers değiştirilmiş index:\n", pd.Series([20,30,40,50], [3,4,5,6]))
print("Sabit değer:\n", pd.Series(5, [0,1,2,3]))
print("Numbers custom index:\n", pd.Series(data=numbers, index=['ı','ıı','ııı','ıv'], name='new'))
print("\n" + 20 * '-' + "\n")

pandas_series = pd.Series([28,36,44,51], [0,1,'c','d'])
print('0. index:', pandas_series[0])
print('d. index:', pandas_series['d'])
print('çoklu index:\n', pandas_series[[0,'c','d']])
# iloc (integer location) index ile seçim yapma anlamına gelir. Serieste sadece satırı seçebiliriz.
print('iloc ilk eleman:', pandas_series.iloc[0])
print('iloc son eleman:', pandas_series.iloc[-1])
print('iloc ilk iki:\n', pandas_series.iloc[:2])
print('iloc son iki:\n', pandas_series.iloc[-2:].values)
print("\n" + 20 * '-' + "\n")

print('boyut ndim:', pandas_series.ndim)
print('dtype:', pandas_series.dtype)
print('shape:', pandas_series.shape)
print('toplam:', pandas_series.sum())
# max(), min(), std(), argmax(), argmin()
print("\n" + 20 * '-' + "\n")

print('seri * 3:\n', pandas_series * 3)
print('seri + 50:\n', pandas_series + 50)
print('karekök:\n', np.sqrt(pandas_series))
print("\n" + 20 * '-' + "\n")

result1 = pandas_series >=50
result2 = pandas_series % 2 == 0

print(pandas_series[result1])
print(result2)
print("\n" + 20 * '-' + "\n")

opel2018 = pd.Series([20,30,40,10],["astra","corsa","insignia","mokka"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

total = opel2018 + opel2019
print(total)