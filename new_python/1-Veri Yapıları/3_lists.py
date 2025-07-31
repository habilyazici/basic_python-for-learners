
# =====================================================
# 1. Listelerle Temel İşlemler
# =====================================================

message = 'Hello There. My name is Sadık Turan'.split()
# print(message[0])
# my_list = [1,2,3]
# my_list = ['bir',2, True, 5.6]
# print(my_list)
list1 = ['one','two','there']
list2 = ['four','five','six']
numbers = list1 + list2
print("Birleştirilmiş liste:", numbers)
print("Uzunluk:", len(numbers))
print("İlk kelime:", message[0])
print("Üçüncü sayı:", numbers[2])
userA = ['Sadık', 36]
userB = ['Çınar', 2]
users = [userA, userB]
print("userA:", userA)
print("userB:", userB)
print("users:", users)
print("users[0][0]:", users[0][0])
print()

# =====================================================
# 2. Listelerle Uygulama ve Sık Kullanılan İşlemler
# =====================================================

arabalar = ['Bmw','Mercedes','Opel','Mazda']
result = len(arabalar)
print("Araba sayısı:", result)
result = arabalar[0]
print("İlk araba:", result)
result = arabalar[3]
print("Dördüncü araba:", result)
result = arabalar[-1]
print("Son araba:", result)
# arabalar[-1]= 'Toyota'
result = arabalar
print("Arabalar listesi:", result)
result = 'Mercedes' in arabalar
print("Mercedes var mı?:", result)
result = arabalar[-2]
print("Sondan ikinci araba:", result)
result = arabalar[0:3]
print("İlk üç araba:", result)
result = arabalar[:3]
print("İlk üç araba (alternatif):", result)
result = arabalar[-2:]
print("Son iki araba:", result)
arabalar[-2:] = ['Toyota','Renault']
print("Güncellenmiş arabalar:", arabalar)
result = arabalar + ['Audi','Nissan']
print("Yeni arabalar listesi:", result)
del arabalar[-1]
print("Son araba silindi:", arabalar)
result = arabalar[::-1]
print("Ters çevrilmiş arabalar:", result)
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]
result = studentA[0]
print("studentA adı:", result)
result = studentB[1]
print("studentB soyadı:", result)
result = studentC[3][1]
print("studentC ikinci notu:", result)
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)
print()

# =====================================================
# 3. Liste Metodları ve Fonksiyonları
# =====================================================

numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
print("min(numbers):", min(numbers))
print("max(numbers):", max(numbers))
print("max(letters):", max(letters))
print("min(letters):", min(letters))
print("numbers[3:6]:", numbers[3:6])
print("numbers[:3]:", numbers[:3])
print("numbers[4:]:", numbers[4:])
numbers[4] = 40
numbers.append(49)
numbers.append(59)
numbers.insert(3, 78)
numbers.insert(-1,52)
# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59)
numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()
print("Sıralı numbers:", numbers)
print("Sıralı letters:", letters)
print("numbers uzunluğu:", len(numbers))
print("letters uzunluğu:", len(letters))
print("numbers.count(10):", numbers.count(10))
print("letters.count('a'):", letters.count('a'))
numbers.clear()
print("Temizlenmiş numbers:", numbers)
print()

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
