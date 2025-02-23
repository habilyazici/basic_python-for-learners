cities = ['barcelona', 'izmir', 'moskova', 'belgrad', 'tahran', 32]
print(cities[0])
print(cities.index('izmir'))
print(len(cities))

cities = ['barcelona', 'izmir', 'moskova', 'belgrad', 'tahran']
cities[0] = 'istanbul'
cities[len(cities):]= ['kahramanmaraş'] 
cities.append('selanik')
cities.insert(4,'kahramanmaraş')
print(cities)
# Burada append methodu sürekli sona ekler ama insert methodu istenilen index yerine ekler. Liste yapılarında update yoktur.

cities = ['barcelona', 'izmir', 'moskova', 'belgrad', 'tahran']
del cities[0]
cities.pop(0) #cities2 = cities.pop(0) içeriye hiçbir şey yazmazsan otomatik olarak en sondakini siler
cities.remove('belgrad')
print(cities)
# del ile silinirse silinen elemana artık ulaşılamaz. Pop ile istenilen eleman alınır.

cities = ['barcelona', 'izmir', 'moskova', 'belgrad', 'tahran']
print(sorted(cities))
cities.sort()
print(cities)
cities.sort(reverse=True) # or cities.reverse()
print(cities)

rakamlarimiz='12312312'
print(list(rakamlarimiz))

str_strings= 'habilyazici00@gmail.com'
my_list = str_strings.split('@')
print(my_list) # split methodu stringi liste yapısına çevirmektedir.
# parantez içerisine hiçbir şey yazmazsan default olarak boşluğa göre ayırır.
print('@'.join(['habilyazici00', 'gmail.com'])) 

dersler= ['matematik', 'türkçe', 'tarih', 'fizik']
dersler2 = dersler
dersler.append('biyokimya')
print(dersler)
print(dersler2)
# Bu şekilde bir değişkeni diğer değişkene bağlarsan ikisi arasında bağlantı olur ve ilkindeki değişiklik ikinciyi etkiler.

türkçe= ['anlatım bozkluğu', 'yapı bilgisi', 'bla bla']
türkçe2 = türkçe[:]
türkçe.append('sıfatlar')
print(türkçe) 
print(türkçe2)
# Eğer bu şekilde bağlarsan sadece o andaki görüntüsünü almış olursun ve ayrı bir liste oraya çıkar.

dersler4= ['matematik', 'türkçe', ['tarih','inkılap'] , 'fizik', 'tarih']
print(dersler4[1].upper())
print(dersler4[len(dersler4)-1].lower())
print(dersler4[2][1])

for num in range(1,10+1):
    print(num)
print(type(num))

numbers2= list(range(1,23))
print(numbers2)

sayi_kareler= [num**2 for num in range(1,11)]
print(sayi_kareler) # list comphereshion yöntemidir bu.

sayilarim= []
for sayi in range(1,11):
    sayilarim.append(sayi**2)
print(sayilarim)

yeniDersler= [['algoritma', 'akış şeması'], ['coğrafya', 'bulutlar'], ['geometri', 'üçgen']]
yeniDersler2= []
for ders_listesi in yeniDersler:
    yeniDersler2.append(ders_listesi[1])
print(yeniDersler2)
