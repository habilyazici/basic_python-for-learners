# Değişkenler ve Sayılar

# --- variables.py ---
maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Değişken Tanımlama Kuralları
# rakam ile başlayamaz
number1 = 10
print(number1)
number1 = 20
print(number1)
number1 += 30
print(number1)
# Büyük küçük harf duyarlılığı
age = 20
AGE = 30
print(age)
print(AGE)
# Türkçe karakter kullanmayalım
yas = 20
_age = 20
x = 1              # int
y = 2.3            # float 
name = "Çınar"     # string
isStudent = True   # bool
# x, y, name, isStudent = (1, 2.3, "Çınar", True)
a = '10'
b = '20'
print(a+b) # => 1020
firstName = "Sadık"
lastName = " Turan"
print(firstName + lastName)  # Sadık Turan

# --- numbers.py ---
print(2+2)

# --- type-conversion.py ---
"""
x = input('1.sayı: ')
y = input('2.sayı: ')
print(type(x))
print(type(y))
toplam = int(x) + int(y)
print(toplam)
"""
x = 5               #int
y = 2.5             #float
name = 'Çınar'      #str
isOnline = True     #bool
# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))
# Type Conversion
# int to float
# x = float(x)
# print(x)
# print(type(x))
# float to int
# y = int(y)
# print(y)
# print(type(y))
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
print(isOnline)
print(type(isOnline))

# --- type-conversion-demo.py ---
'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    * Yarı çapı verilen bir dairenin alan ve çevresini 
    hesaplayınız. (r: 3.14)
'''
pi = 3.14
r = float(input("yarı çap: "))
alan = pi * (r ** 2)
print(type(alan))
cevre = 2 * pi * r
print(type(cevre))
print("alan: "+ str(alan) + " çevre: "+ str(cevre))
