
# =====================================================
# 1. Tuple İşlemleri
# =====================================================

list = [1, 2, 3]
tuple = (1, 'iki', 3)
# print(type(list))
# print(type(tuple))
# print(list[2])
# print(tuple[2])
# print(len(tuple))
# print(len(list))
list = ['ali','veli']
tuple = ('damla','ayşe','ayşe')
names = ('demet','emel','ayşe') + tuple
print(names)
list[0] = 'ahmet'
# tuple[0] = 'deniz'
print(tuple.count('ayşe'))
print(tuple.index('ayşe'))
print(list)
print(tuple)
print()


# --- sets.py ---
fruits = { 'orange', 'apple', 'banana'}
# print(fruits[0]) indekslenemez
for x in fruits:
    print(x)
fruits.add('cherry')
fruits.update(['mango','grape','apple'])
fruits.remove('mango')
fruits.discard('apple')
fruits.pop()
fruits.clear()
print(fruits)
# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))
print()


# --- dictionary.py ---
# key - value
# 41 => kocaeli 34 => istanbul
# sehirler = ['kocaeli','istanbul']
# plakalar = [41, 34]
# print(plakalar[sehirler.index('istanbul')])
# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34
# plakalar = { 'kocaeli' : 41, 'istanbul': 34 }
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])
# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'
# print(plakalar)
users = {
    'sadikturan': {
        'age': 36,        
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'cinarturan': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}
print(users['cinarturan']['roles'][0])
print()

# --- dictionary-demo.py ---
'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.
    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''
ogrenciler = {}
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")
# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }
ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")
ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")
ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
print('*'*50)
ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
