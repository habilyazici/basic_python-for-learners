sehirler = ['kocaeli','istanbul','ankara','izmir','rize']
plakalar = [41, 34, 6, 35, 53]
print(plakalar[sehirler.index('istanbul')])
plakalar_dict = { 'kocaeli' : 41, 'istanbul': 34 }
print(plakalar_dict['kocaeli'])
plakalar_dict['ankara'] = 6
plakalar_dict['kocaeli'] = 'new value'
print(plakalar_dict)
print("\n" + 20 * '-' + "\n")

users = {
    'selimturan': {
        'age': 36,        
        'roles': ['user'],
        'email': 'selim@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'habilyazici': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'habil@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}
print(users['selimturan']['email'])
print(users['habilyazici']['roles'][0])
print(users.get('mehmetturan'))
users['selimturan']['roles'].append('db_admin')
print("\n" + 20 * '-' + "\n")

ogrenciler = {

}
ogrNo = int(input("öğrenci no: "))
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")
ogrenciler.update({
    ogrNo: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
ogrNo = int(input('Bilgi almak istediğiniz öğrenci no: '))
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenciler[ogrNo]['ad']} soyadı: {ogrenciler[ogrNo]['soyad']} ve telefonu ise {ogrenciler[ogrNo]['telefon']}")
print("\n" + 20 * '-' + "\n")

list1= []
list2= list()
string= ''
string2= str()
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
print("\n" + 20 * '-' + "\n")