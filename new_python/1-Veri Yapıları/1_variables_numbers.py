# =====================================================
# 1. Değişkenler ve Temel Veri Tipleri
# =====================================================

# Maaş ve Vergi Hesaplama Örneği
maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print("Ali'nin net maaşı:", maasAli - (maasAli * vergi))
print("Ahmet'in net maaşı:", maasAhmet - (maasAhmet * vergi))
print()

# Değişken Tanımlama Kuralları
# - Değişken isimleri rakam ile başlayamaz
# - Büyük/küçük harf duyarlıdır
# - Türkçe karakter kullanmaktan kaçının
number1 = 10
number1 = 20
number1 += 30

print("number1:", number1)
number1 = 20
print("number1:", number1)
number1 += 30
print("number1:", number1)
print()

age = 20
AGE = 30
yas = 20
_age = 20

print("age:", age)
print("AGE:", AGE)
yas = 20
_age = 20
print()

# Temel veri tipleri
x = 1              # int
y = 2.3            # float 
name = "Çınar"     # string
isStudent = True   # bool

print("x:", x, "y:", y, "name:", name, "isStudent:", isStudent)
print()

# Çoklu atama örneği (yorum satırı)
# x, y, name, isStudent = (1, 2.3, "Çınar", True)

# String birleştirme örnekleri
a = '10'
b = '20'
print("a+b (string):", a+b) # => 1020
firstName = "Sadık"
lastName = " Turan"

print("Ad Soyad:", firstName + lastName)  # Sadık Turan
print()

 
# =====================================================
# 2. Sayılar ve Basit İşlemler
# =====================================================
print("2+2 =", 2+2)

print("2+2 =", 2+2)
print()

# =====================================================
# 3. Tip Dönüşümleri (Type Conversion)
# =====================================================
# Kullanıcıdan alınan veriler string olarak gelir
"""
x = input('1.sayı: ')
y = input('2.sayı: ')
print(type(x))
print(type(y))
toplam = int(x) + int(y)
print(toplam)
"""
# Temel tipler ve dönüşümler
x = 5               # int
y = 2.5             # float
name = 'Çınar'      # str
isOnline = True     # bool
# print(type(x))
# print(type(y))
# print(type(name))

# Temel tipler ve dönüşümler
x = 5               # int
y = 2.5             # float
name = 'Çınar'      # str
isOnline = True     # bool
# print(type(x))
# print(type(y))
# print(type(name))
print()

# =====================================================
# 2. Tip Dönüşümleri (Type Conversion)
# =====================================================
# Kullanıcıdan alınan veriler string olarak gelir
"""
x = input('1.sayı: ')
y = input('2.sayı: ')
print(type(x))
print(type(y))
toplam = int(x) + int(y)
print(toplam)
"""
# Temel tipler ve dönüşümler
x = 5               # int
y = 2.5             # float
name = 'Çınar'      # str
isOnline = True     # bool
# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))
# int to float
# x = float(x)
# print(x)
# print(type(x))
# float to int
# y = int(y)
# print(y)
# print(type(y))
# str birleştirme
# result = str(x) + str(y)
# print(result)
# print(type(result))
# bool to str
# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))
# bool to int
isOnline = False
isOnline = int(isOnline)

print("isOnline (int):", isOnline)
print(type(isOnline))
print()

# =====================================================
# 3. Uygulama: Daire Alanı ve Çevresi Hesaplama
# =====================================================
'''
Daire Alanı   : πr²
Daire Çevresi : 2πr    
* Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (pi: 3.14)
'''
pi = 3.14
r = float(input("Yarı çapı girin: "))
alan = pi * (r ** 2)
print("Alan tipi:", type(alan))
cevre = 2 * pi * r
print("Çevre tipi:", type(cevre))
print("Dairenin alanı:", alan, "Çevresi:", cevre)
