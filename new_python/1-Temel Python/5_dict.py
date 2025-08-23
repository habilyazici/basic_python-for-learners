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
print(users1.get('asdfdasdf'))
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


list1= []
list2= list()
string= ''
tuple1= ()
tuple2= tuple()
set1= set()
dict1= {}
dict2= dict()

dict1= {'mehmet': 12, 'selim': 53, 'ali': 89}
for k,v in dict1.items():
    if v>=50:
        print(f'{k} nın aldığı not {v} ve : {k} GEÇTİ')
    else:
        print(f'{k} nın aldığı not {v} ve : KALDI')

musteriler= {'Elon Musk': {'doğum yeri': 'izmir', 'yaş': 56 , 'medeni durum': 'evli'}, 
             'Habil Yazıcı': {'doğum yeri': 'rize', 'yaş': 23 , 'medeni durum': 'bekar'}}
print(musteriler['Habil Yazıcı']['yaş'])