# Hata (Error) örnekleri
# print(a)            # NameError: 'a' tanımlı değil
# int('1a2')          # ValueError: Geçersiz sayı dönüşümü
# print(10/0)         # ZeroDivisionError: Sıfıra bölme
# print('denem'e)     # SyntaxError: Yazım hatası

liste = ["1","2","5a","10b","abc","10","50"]
for x in liste:
    try:
        print(int(x))
    except ValueError:
        continue
print("\n" + 20 * '-' + "\n")

while True:
    sayi = input('sayı: ')
    if sayi == 'q':
        break
    try:
        result = float(sayi)
        print('girdiğiniz sayı: ', result)
        break
    except ValueError:
        print('geçersiz sayı')
print("\n" + 20 * '-' + "\n")

def checkPassword(parola):
    turkce_karakterler = 'şçğüöıİ'
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola türkçe karakter içeremez.')
    print('geçerli parola')
hak = 3
while hak > 0:
    parola = input('parola: ')
    try:
        checkPassword(parola)
        break
    except TypeError as err:
        print(err)
        hak -= 1
        if hak == 0:
            print('Hakkınız doldu. Program sonlandı.')
        else:
            print(f'Kalan deneme hakkınız: {hak}')
print("\n" + 20 * '-' + "\n")

def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError('Negatif değer') # direkt Exception('Negatif değer') veya Exception.
    result = 1
    for i in range(1, x+1):
        result *= i
    return result
for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except Exception as err:
        print(err)
        continue
    print(y)
print("\n" + 20 * '-' + "\n")

def factorial(number):
    if not isinstance(number, int): # boolean döner
        raise TypeError("number must be an integer")
    if not number >=0:
        raise ValueError("number must be zero or positive")
    if number <= 1:
        return 1
    return number * factorial(number - 1)
try:
    print(factorial("4"))
except Exception as ex:
    print(ex)
print("\n" + 20 * '-' + "\n")

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print('Hatalı işlem!')
    print(e)
print("\n" + 20 * '-' + "\n")

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('Hatalı işlem!', ex)
    else:
        break
    # try kısmıı başarılı olursa else çalışır. finally hep çalışır.
    finally:
        print('try except sonlandı.')
print("\n" + 20 * '-' + "\n")

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name
        self.year = year
try:
    p = Person("Aliiiiiiiiiiii", 1989)
except Exception as ex:
    print("Person oluşturulurken hata oluştu:", ex)