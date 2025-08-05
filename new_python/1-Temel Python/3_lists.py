list1 = ['one','two','there']
list2 = ['four','five','six']
numbers1 = list1 + list2
message2 = 'Hello There. My name is Sadık Turan'.split()
print(message2[0])
my_list1 = [1,2,3]
my_list2 = ['bir',2, True, 5.6]
print(my_list1)
print(my_list2)
print("Birleştirilmiş liste:", numbers1)
print("Uzunluk:", len(numbers1))
print("İlk kelime:", message2[0])
print("Üçüncü sayı:", numbers1[2])
userA1 = ['Sadık', 36]
userB1 = ['Çınar', 2]
users1 = [userA1, userB1]
print("userA:", userA1)
print("userB:", userB1)
print("users:", users1)
print("users[0][0]:", users1[0][0])
print()
# =====================================================

numbers = list1 + list2
message2 = 'Hello There. My name is Sadık Turan'.split()
print(message2[0])
my_list1 = [1,2,3]
my_list2 = ['bir',2, True, 5.6]
print(my_list1)
print(my_list2)
list1 = ['one','two','there']
list2 = ['four','five','six']
# ...existing code...

# =====================================================
# 2. Listelerle Uygulama ve Sık Kullanılan İşlemler
arabalar1 = ['Bmw','Mercedes','Opel','Mazda']
print("Araba sayısı:", len(arabalar1))
print("İlk araba:", arabalar1[0])
print("Dördüncü araba:", arabalar1[3])
print("Son araba:", arabalar1[-1])
print("Arabalar listesi:", arabalar1)
print("Mercedes var mı?:", 'Mercedes' in arabalar1)
print("Sondan ikinci araba:", arabalar1[-2])
print("İlk üç araba:", arabalar1[0:3])
print("İlk üç araba (alternatif):", arabalar1[:3])
print("Son iki araba:", arabalar1[-2:])
arabalar1[-2:] = ['Toyota','Renault']
print("Güncellenmiş arabalar:", arabalar1)
print("Yeni arabalar listesi:", arabalar1 + ['Audi','Nissan'])
del arabalar1[-1]
print("Son araba silindi:", arabalar1)
print("Ters çevrilmiş arabalar:", arabalar1[::-1])
studentA1 = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB1 = ['Sena','Turan',1999,[80,80,70]]
studentC1 = ['Ahmet','Turan',1998,[80,70,90]]
print("studentA adı:", studentA1[0])
print("studentB soyadı:", studentB1[1])
print("studentC ikinci notu:", studentC1[3][1])
print(f"{studentA1[0]} {studentA1[1]} {2019-studentA1[2]} yaşında ve not ortalaması {(studentA1[3][0] + studentA1[3][1] + studentA1[3][2])/3}")
print()
# =====================================================

arabalar[-2:] = ['Toyota','Renault']
del arabalar[-1]
arabalar1 = ['Bmw','Mercedes','Opel','Mazda']
print("Araba sayısı:", len(arabalar1))
print("İlk araba:", arabalar1[0])
print("Dördüncü araba:", arabalar1[3])
print("Son araba:", arabalar1[-1])
print("Arabalar listesi:", arabalar1)
print("Mercedes var mı?:", 'Mercedes' in arabalar1)
print("Sondan ikinci araba:", arabalar1[-2])
print("İlk üç araba:", arabalar1[0:3])
print("İlk üç araba (alternatif):", arabalar1[:3])
print("Son iki araba:", arabalar1[-2:])
print("Son araba silindi:", arabalar1)
# ...existing code...
studentC1 = ['Ahmet','Turan',1998,[80,70,90]]
print("studentA adı:", studentA1[0])
print("studentB soyadı:", studentB1[1])
print("studentC ikinci notu:", studentC1[3][1])
print(f"{studentA1[0]} {studentA1[1]} {2019-studentA1[2]} yaşında ve not ortalaması {(studentA1[3][0] + studentA1[3][1] + studentA1[3][2])/3}")
print()

# =====================================================
# 3. Liste Metodları ve Fonksiyonları
numbers2 = [1, 10, 5, 16, 4, 9, 10]
letters2 = ['a', 'g', 's', 'b', 'y', 'a', 's']
print("min(numbers):", min(numbers2))
print("max(numbers):", max(numbers2))
print("max(letters):", max(letters2))
print("min(letters):", min(letters2))
print("numbers[3:6]:", numbers2[3:6])
print("numbers[:3]:", numbers2[:3])
print("numbers[4:]:", numbers2[4:])
numbers2[4] = 40
numbers2.append(49)
numbers2.append(59)
numbers2.insert(3, 78)
numbers2.insert(-1,52)
numbers2.pop()
numbers2.pop(0)
numbers2.pop(-1)
numbers2.remove(59)
numbers2.sort()
numbers2.reverse()
letters2.sort()
letters2.reverse()
print("Sıralı numbers:", numbers2)
# =====================================================


# =====================================================
# 4. Liste Uygulama Soruları
# =====================================================

names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]
# names.append('Cenk')
# names.insert(0, 'Sena')
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')
# names.remove('Deniz')
# names.pop()
# names.pop(1)
# index  = names.index('Deniz')
# names.pop(index)
# result = 'Ali' in names
# result = names.index('Ali')
# names.reverse()
# names.sort()
# years.sort()
# str = "Chevrolet,Dacia"
# result = str.split(',')
# min = min(years)
# max = max(years)
# print(min, max)
# result = years.count(1998)
# years.clear()

markalar = []
for i in range(3):
    marka = input(f"{i+1}. markayı girin: ")
    markalar.append(marka)
print("Girilen markalar:", markalar)
