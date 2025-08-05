# =====================================================
# Operatörler, Koşullar ve Döngüler - Toplu Notlar
# =====================================================

# 1. Karşılaştırma Operatörleri
# -----------------------------
a, b, c, d = 5, 5, 10, 4
password = '1234'
username = 'sadikturan'
print(a == b)
print(a == c)
print('sdktrn'== username)
print('sadikturan'== username)
print(a != b)
print(a != c)
print(a > c)
print(a < c)
print(a >= b)
print(c <= b)
print(True == 1)
print(False == 0)
print(False + True + 40)

# 2. Mantıksal Operatörler
# ------------------------
x = 5
hak = 0
devam = 'e'
print((x > 5) and (x < 10))
print((hak > 0) and (devam == 'e'))
print((x > 0) or (x % 2 == 0))
print(not(x > 0))
print(((x>5) and (x<10)) and (x%2==0))

# 3. Atama Operatörleri ve Temel Döngüler
# ---------------------------------------
x, y, z = 2, 5, 10
values = 1, 2, 3, 4, 5
print(values)
print(type(values))
x, y, *z = values
print(x, y, z)
print(x, y, z[1])

numbers = [1,2,3,4,5]
for a in numbers:
    print('Hello')
names = ['çınar','sadık','sena']
for name in names:
    print(f'my name is {name}')
name = 'Sadık Turan'
for n in name:
    print(n)
tuple_list = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple_list:
    print(a,b)
d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(key, value)

x = 1
while x <= 10:
    if x % 2==1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1
print('bitti...')

# 4. For ve While Döngüsü Uygulamaları
# ------------------------------------
sayilar = [1,3,5,7,9,12,19,21]
# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
# 2- Sayilar listesinde sayıların toplamı kaçtır ?
# 3- Sayilar listesindeki tek sayıların karesini alınız.
# sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
# urunler = [ ... ]
# 5- Ürünlerin fiyatları toplamı nedir ?
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

# while ile uygulamalar
# 1: sayilar listesini while ile ekrana yazdırın.
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.

# 5. break, continue, range, enumerate, zip, list comprehensions
# -------------------------------------------------------------
# break-continue örnekleri
x = 0
result = 0
while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x
print(f'toplam: {result}')

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(list(zip(list1, list2, list3)))
for item in zip(list1, list2, list3):
    print(item)
for a,b,c in zip(list1, list2, list3):
    print(a,b,c)

numbers = [x for x in range(10)]
print(numbers)
numbers = [x**2 for x in range(10)]    
print(numbers)
numbers = [x*x for x in range(10) if x%3==0]
print(numbers)

# 6. Karışık Uygulamalar ve Mini Projeler
# ---------------------------------------
# Sayi tahmin oyunu
# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
# import random
# sayi = random.randint(1,10)
# can = int(input('kaç hak kullanmak istersiniz: '))
# hak = can
# sayac = 0
# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('tahmin: '))
#     if sayi == tahmin:
#         print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1) }')
#         break
#     elif sayi > tahmin:
#         print('yukarı')
#     else:
#         print('aşağı')
#     if hak == 0:
#         print(f'hakkınız bitti. Tutulan sayı : {sayi}')

# Asal sayı kontrolü
# sayi = int(input('sayı: '))
# asalmi = True
# if sayi == 1:
#     asalmi = False
# for i in range(2, sayi):
#     if (sayi % i == 0):
#         asalmi = False
#         break
# if asalmi:
#     print('sayı asaldır.')
# else:
#     print('sayı asal değildir.')
