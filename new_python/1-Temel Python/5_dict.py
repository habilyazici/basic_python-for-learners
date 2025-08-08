# key - value
sehirler = ['kocaeli','istanbul']
plakalar = [41, 34]
print(plakalar[sehirler.index('istanbul')])
# print(plakalar['kocaeli']) => 41
plakalar_dict = { 'kocaeli' : 41, 'istanbul': 34 }
print(plakalar_dict['kocaeli'])
plakalar_dict['ankara'] = 6
plakalar_dict['kocaeli'] = 'new value'
print(plakalar_dict)
print("\n" + 20 * '-' + "\n")

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
print(users1['sadikturan']['email'])
users1['sadikturan']['roles'].append('admin')
print("\n" + 20 * '-' + "\n")

## Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
## Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
ogrenciler = {

}
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
print("\n" + 20 * '-' + "\n")
ogrNo = input('öğrenci no: ') 
print(ogrenciler[ogrNo])
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenciler[ogrNo]['ad']} soyadı: {ogrenciler[ogrNo]['soyad']} ve telefonu ise {ogrenciler[ogrNo]['telefon']}")
