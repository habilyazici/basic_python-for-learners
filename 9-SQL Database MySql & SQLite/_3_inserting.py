import mysql.connector

def showTypes():
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "SELECT * FROM turler"
    cursor.execute(sql)

    result = cursor.fetchall()
    for tur in result:
        print(f'Tür ID: {tur[0]}, Tür Adı: {tur[1]}')
    connection.close()

def insertFilm(Ad, Tarih, IMDB_Puan):
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "INSERT INTO filmler(Ad, Tarih, IMDB_Puan) VALUES (%s, %s, %s)" 
    values = (Ad,Tarih,IMDB_Puan)

    try:
        cursor.execute(sql,values)
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        film_id = cursor.lastrowid
        print(f'son eklenen kaydın idsi: {film_id}')

        showTypes()
        print("\n" + 20 * '-' + "\n")

        tur_id = int(input('Tür ID giriniz: '))
        sql2 = "INSERT INTO film_tur (film_id, tur_id) VALUES (%s, %s)"
        values2 = (film_id, tur_id)
        try:
            cursor.execute(sql2, values2)
            connection.commit()
            print(f'film_tur tablosuna eklendi: film_id={film_id}, tur_id={tur_id}')
        except mysql.connector.Error as err:
            print('hata:', err)
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        cursor.close()
        connection.close()
        print('database bağlantısı kapandı.')

insertFilm( "merhaba dünya", "2023,01,01", 8.5)

# Gönderdiğin veri tiplerine iyice dikkat et mysql veritabanında ne yazarsa ona göre kayıt yapar.

def insertFilms(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="", database="sinema")
    cursor = connection.cursor()

    sql = "INSERT INTO filmler(Ad, Tarih, IMDB_Puan) VALUES (%s, %s, %s)" 
    values = list
    # birden fazla kayıt eklemek için liste içerisinde tuple oluşturulur
    cursor.executemany(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        cursor.close()
        connection.close()
        print('database bağlantısı kapandı.')

list = []
while True:
    Ad = input('film adı: ')
    Tarih = input('film tarihi: ')
    IMDB_Puan = float(input('film IMDB puanı: '))

    list.append((Ad, Tarih, IMDB_Puan))

    result = input('devam etmek istiyor musunuz? (e/h)')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)
        insertFilms(list)
        break
