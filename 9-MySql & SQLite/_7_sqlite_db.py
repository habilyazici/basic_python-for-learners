import sqlite3
# sqlite sunucusuzdur yerel çalışan bir dosyadır, https://sqliteonline.com/ veya sqlite uygulamalarından biriyle görsel iletişim sağlanabilir.

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
myConnection = sqlite3.connect("chinook.db")
myCursor = myConnection.cursor()

myCursor.execute("select * from customers")
result = myCursor.fetchall()

for i in result:
    print(i)

myConnection.close()