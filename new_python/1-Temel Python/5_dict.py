# =====================================================
# Dictionary (Sözlük) İşlemleri
# =====================================================

# key - value
# 41 => kocaeli 34 => istanbul
sehirler = ['kocaeli','istanbul']
plakalar = [41, 34]
print(plakalar[sehirler.index('istanbul')])
# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34
plakalar_dict = { 'kocaeli' : 41, 'istanbul': 34 }
print(plakalar_dict['kocaeli'])
print(plakalar_dict['istanbul'])
plakalar_dict['ankara'] = 6
plakalar_dict['kocaeli'] = 'new value'
print(plakalar_dict)

users1 = {
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
print(users1['cinarturan']['roles'][0])
print()

## Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
## Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
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
