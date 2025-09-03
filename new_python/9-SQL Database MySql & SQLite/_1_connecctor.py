import mysql.connector

connection = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "",
    database = "sinema"
)

if connection.is_connected():
    print("Connection successful")
else:
    print("Connection failed")


