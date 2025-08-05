# Fonksiyonlar ve Parametreler

def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('Çınar')
msg = sayHello('Ada')
print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)
print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')
EmekliligeKacYilKaldi(1983, 'Ali')

# *args ve **kwargs kullanımı

def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum
print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30,50,60,10,20))

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayUser(name= 'Çınar', age = 2, city = 'istanbul')
displayUser(name= 'Ada', age = 12, city = 'kocaeli', phone = '123132')
displayUser(name= 'Yiğit', age = 14, city = 'ankara', phone = '123132', email= 'yigit@gmail.com')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)

# Fonksiyon uygulamaları
# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon
# def yazdir(kelime, adet):
#     print(kelime * adet)
# yazdir('Merhaba\n', 10)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
# def listeyeCevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste
# result = listeyeCevir(10,20,30,'Merhaba')
# print(result)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon
# def asalSayilariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))
# asalSayilariBul(sayi1, sayi2)

# Encapsulation ve iç içe fonksiyonlar
# def greeting(name):
#     print('hello ', name)
# print(greeting('ali'))
# print(greeting)
# sayHello = greeting
# del sayHello
# print(sayHello)
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)
# outer(10)
# inner_increment(10)

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

# Scope örnekleri
global_x = 'global x'
def function():
    print(global_x)
function()
print(global_x)

name = 'Çınar'
def changeName(new_name):
    global name
    name = new_name
    print(name)
changeName('Ada')
print(name)

name = 'global string'
def greeting():
    def hello():
        print('hello '+ name)
    hello()
greeting()
