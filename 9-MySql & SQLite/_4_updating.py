import mysql.connector
from _2_selecting import getFilms, getFilmById

getFilms()
def updateFilm(id, name, IMDB_Puan):
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "Update filmler Set Ad= %s, IMDB_Puan= %s where Film_ID= %s"
    values = (name, IMDB_Puan, id)
    cursor.execute(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt güncellendi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        cursor.close()
        connection.close()
        print('database bağlantısı kapandı.')

updateFilm(1, 'Yeşil Yol2', 2001)
getFilmById(1)