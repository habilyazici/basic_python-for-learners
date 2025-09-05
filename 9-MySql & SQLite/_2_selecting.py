import mysql.connector

def getFilms():
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    # cursor.execute('Select * From filmler')
    cursor.execute("Select * From filmler order by Film_ID")

    try:
        result = cursor.fetchall()    
        for film in result:
            print(f'id: {film[0]} film adı: {film[1]} IMDB puanı: {film[2]}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        cursor.close()
        connection.close()
        print('database bağlantısı kapandı.')
getFilms()


def getFilmById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "Select * From filmler Where Film_ID=%s"
    params = (id,)
    # virgül sayesinde python bunu bir tuple olarak algılar
    cursor.execute(sql, params)

    result = cursor.fetchone()    
    print(f'id: {result[0]} film adı: {result[1]} IMDB puanı: {result[2]}')
    cursor.close()
    connection.close()

getFilmById(3)