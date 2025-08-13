# 10_hata_nedir.py
# error => hata
# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError
# error handling => hata yönetimi

# 11_hata_ornekleri.py
liste = ["1","2","5a","10b","abc","10","50"]
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue
# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
# while True:
#     sayi = input('sayı: ')
#     if sayi == 'q':
#         break
#     try:
#         result = float(sayi)
#         print('girdiğiniz sayı: ', result)
#         break
#     except ValueError:
#         print('geçersiz sayı')
#         continue
# 3: Girilen parola içinde türkçe karakter hatası veriniz.
# def checkPassword(parola):
#     turkce_karakterler = 'şçğüöıİ'
#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('Parola türkçe karakter içeremez.')
#         else:
#             pass
#     print('geçerli parola')
# parola = input('parola: ')
# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)
# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError('Negatif değer')
    result = 1
    for i in range(1, x+1):
        result *= i
    return result
for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not number >=0:
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)
try:
    print(factorial("4"))
except Exception as ex:
    print(ex)
print("\n" + 20 * '-' + "\n")

# 12_hata_yonetimi.py
# error handling => hata yönetimi
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz')
#     print(e)
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz')
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz', ex)
    else:
        break
    finally:
        print('try except sonlandı.')

# 13_raise_kullanimi.py
# x = 10
# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz.")
# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("parola en az 7 karakter olmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("parola alpha numeric karakter içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("parola boşluk içermemelidir.")
#     else:
#         print("geçerli parola")
# password = "1234567aA_"
# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola: else")
# finally:
#     print("validation tamamlandı.")
class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name
p = Person("Aliiiiiiiiiiii", 1989)
