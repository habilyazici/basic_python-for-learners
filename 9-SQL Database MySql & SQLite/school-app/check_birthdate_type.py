import mysql.connector

# Bağlantı bilgilerini kendi veritabanına göre düzenle
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sinema'
)
cursor = conn.cursor()

# Örnek sorgu: teacher tablosundan doğum tarihi al
cursor.execute("SELECT birthdate FROM teacher LIMIT 1")
result = cursor.fetchone()

if result:
    birthdate = result[0]
    print(f"Value: {birthdate}")
    print(f"Type: {type(birthdate)}")
else:
    print("No data found.")

cursor.close()
conn.close()
