a, b, c, d = 5, 5, 10, 4
username = 'sadikturan'
password = '1234'
print(a == b)
print('sadikturan'== username)
print(a != b)
print(a < c)
print(c <= b)
print(True == 1)
print(False + True + 40)
print("\n" + 20 * '-' + "\n")

x = 5
hak = 0
devam = 'e'
print((hak > 0) and (devam == 'e'))
print((x > 0) or (x % 2 == 0))
print(not(x > 0))
print(((x>5) and (x<10)) and (x%2==0))
print("\n" + 20 * '-' + "\n")

values = (1, 2, 3, "mehmet", 5)
print(type(values))
x, y, *z = values
# bir yıldız liste'ye çevirir iki yıldız dictionary'ye çevirir
print("sırasıyla x, y, z: ", x, y, z)
print(type(x))
print(type(z))
print(x, y, z[1])
print("\n" + 20 * '-' + "\n")

names = ['çınar','sadık','sena']
for name in names:
    print(f'my name is {name}')
name = 'Sadık Turan'
for n in name:
    print(n)
print("\n" + 20 * '-' + "\n")

tuple_list = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple_list:
    print(a,b)

d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(key, value)
print("\n" + 20 * '-' + "\n")

x = 1
while x <= 10:
    if x % 2==1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1
print("\n" + 20 * '-' + "\n")

sayilar = [1,3,5,7,9,12,19,21]
for s in sayilar:
    if s % 3 == 0:
        print(f'{s}, 3\'ün katıdır.')

print(f'Sayıların toplamı: {sum(sayilar)}')
print(f'Tek sayıların kareleri: {[s for s in sayilar if s % 2 == 1]}')
print(f'Tek sayıların kareleri: {[s**2 for s in sayilar if s % 2 == 1]}')

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
kucuk_sehirler = [sehir for sehir in sehirler if len(sehir) <= 5]
print(f'5 karakter veya daha kısa şehirler: {kucuk_sehirler}')
print("\n" + 20 * '-' + "\n")

numbers = [x**2 for x in range(10)]    
print(numbers)
numbers = [x*x for x in range(10) if x%3==0]
print(numbers)
print("\n" + 20 * '-' + "\n")

urunler = []
adet = int(input("Kaç ürün eklemek istersiniz? "))
for i in range(adet):
    ad = input(f"{i+1}. ürün adı: ")
    fiyat = float(input(f"{i+1}. ürün fiyatı: "))
    urunler.append({'ad': ad, 'fiyat': fiyat})

toplam_fiyat = sum([urun['fiyat'] for urun in urunler])
print(f"Ürünlerin toplam fiyatı: {toplam_fiyat}")

en_fazla_5000 = [urun for urun in urunler if urun['fiyat'] <= 5000]
for urun in en_fazla_5000:
    print(f" fiyatı en fazla 5000 olan ürün: {urun['ad']} - {urun['fiyat']}")
print("\n" + 20 * '-' + "\n")

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
for item in zip(list1, list2, list3):
    print(item)
print(list(zip(list1, list2, list3)))

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)
print("\n" + 20 * '-' + "\n")

import random
sayi = random.randint(1,10)
can = int(input('kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1) }')
        break
    elif sayi > tahmin:
        print('yukarı çıkın')
    else:
        print('aşağı inin')
    if hak == 0:
        print(f'hakkınız bitti. Tutulan sayı : {sayi}')

sayi = int(input('sayı: '))
asalmi = True
if sayi == 1:
    asalmi = False
for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break
if asalmi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')
