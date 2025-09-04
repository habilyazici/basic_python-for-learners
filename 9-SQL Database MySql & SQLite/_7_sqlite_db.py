import sqlite3
# sqlite sunucusuzdur yerel çalışan bir dosyadır, https://sqliteonline.com/ veya sqlite uygulamalarından biriyle görsel iletişim sağlanabilir

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

cursor.execute("select * from customers")
result = cursor.fetchall()

for i in result:
    print(i)

connection.close()