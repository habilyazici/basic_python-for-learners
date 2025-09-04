import mysql.connector
from _2_selecting import getFilms

def deleteFilm(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "delete from filmler where Film_ID=%s"
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt silindi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

deleteFilm(14)
getFilms()