# Dictionaries veri yapısında herhangi bir varlığa daha iyi bir şekilde tanımlama yapabiliriz. Verilere indexle değil isimle erişilir.
monster_1= {'name': 'guru', 'power': 11 , 'color': 'red'}
print(monster_1['name'])
print(monster_1.get('asdfdasdf'))
print(monster_1)
print(monster_1.keys()) # keys OR values OR items

monster_1['position']= 12
monster_1.update({'name': 'HABİL', 'mevzi': 'stopper'})
del monster_1['color']
monster_1.pop('name')
print(monster_1)

monster_2= {'name': 'guru', 'power': 11 , 'color': 'red' }
for x in monster_2:
    print(x)
# Dictionaries yapısında for döngüsü default olarak keyleri döndürmektedir. İstenilen veri için 'for x in monster_2.values():
monster_2.clear() # del monster_2
print(monster_2)

yeni_list= [
    {'name': 'adam', 'soyad': 'smith'},
    {'name': 'havva', 'soyad': 'cennnet'}
]
print(yeni_list[0]['soyad'])

list1= []
list2= list()
string= ''
tuple1= ()
tuple2= tuple()
set1= set()
dict1= {}
dict2= dict()

arkadaslar= {'selim': 22, 'mehmet': 23, 'ahmet': 65}
print(sum(arkadaslar.values())//(len(arkadaslar)))

my_dict3= {'numbers3': [22,32,54,34,32,61,13]}
for liste in my_dict3.values():
    my_list3= []
    for v in liste:
        my_list3.append(v**2)
my_dict3['numbers3'] = my_list3
print(my_dict3)

my_dict3= {'numbers3': [22,32,54,34,32,61,13], 'numbers6': [12,23,234]}
my_list3= []
for num in my_dict3['numbers3']:
    my_list3.append(num**2)
my_dict3['numbers3'] = my_list3
print(my_dict3)

numbers= {x: x**2 for x in range(1,11)}
print(numbers)

dict1= {'mehmet': 12, 'selim': 53, 'ali': 89}
for k,v in dict1.items():
    if v>=50:
        print(f'{k} nın aldığı not {v} ve : {k} GEÇTİ')
    else:
        print(f'{k} nın aldığı not {v} ve : KALDI')

musteriler= {'Elon Musk': {'doğum yeri': 'izmir', 'yaş': 56 , 'medeni durum': 'evli'}, 
             'Habil Yazıcı': {'doğum yeri': 'rize', 'yaş': 23 , 'medeni durum': 'bekar'}}
print(musteriler['Habil Yazıcı']['yaş'])