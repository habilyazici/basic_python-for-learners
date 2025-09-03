import mysql.connector

def getFilms():
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    # cursor.execute('Select * From filmler')
    cursor.execute('Select Film_ID, AD, tarih From filmler')

    result = cursor.fetchone()
    print(result)

    print(f'filmin idsi: {result[0]} adı: {result[1]} tarihi: {result[2]}')
    print('-------------------')
    
    result = cursor.fetchall()    
    for film in result:
        print(f'filmin idsi: {film[0]} adı: {film[1]} tarihi: {film[2]}')

getFilms()

def getFilm():
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    cursor.execute("Select * From filmler Order By Ad, IMDB_Puan")

    try:
        result = cursor.fetchall()    
        for film in result:
            print(f'id: {film[0]} film adı: {film[1]} IMDB puanı: {film[2]}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')
getFilm()

def getFilmById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "Select * From filmler Where Film_ID=%s"
    params = (id,)
    # virgül sayesinde python bunu bir tuple olarak algılar
    cursor.execute(sql, params)

    result = cursor.fetchone()    
    print(f'id: {result[0]} film adı: {result[1]} IMDB puanı: {result[2]}')
    connection.close()

getFilmById(3)