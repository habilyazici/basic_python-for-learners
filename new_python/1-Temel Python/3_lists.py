list1 = ['one','two','there']
list2 = ['four','five','six']
numbers1 = list1 + list2
print("Birleştirilmiş liste:", numbers1)
print("Uzunluk:", len(numbers1))
print("Üçüncü sayı:", numbers1[2])
print("\n" + 20 * '-' + "\n")

userA1 = ['Sadık', 36]
userB1 = ['Çınar', 2]
users1 = [userA1, userB1]
print("users:", users1)
print("users[0][0]:", users1[0][0])
print("\n" + 20 * '-' + "\n")

arabalar1 = ['Bmw','Mercedes','Opel','Mazda']
print("Araba sayısı:", len(arabalar1))
print("İlk araba:", arabalar1[0])
print("Son araba:", arabalar1[-1])
print("Mercedes var mı?:", 'Mercedes' in arabalar1)
arabalar1[-2:] = ['Toyota','Renault']
print("Güncellenmiş arabalar:", arabalar1)
print("Yeni arabalar listesi:", arabalar1 + ['Audi','Nissan'])
del arabalar1[-1]
print("Ters çevrilmiş arabalar:", arabalar1[::-1])
print("\n" + 20 * '-' + "\n")

studentA1 = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB1 = ['Sena','Turan',1999,[80,80,70]]
studentC1 = ['Ahmet','Turan',1998,[80,70,90]]
print("studentA adı:", studentA1[0])
print("studentB soyadı:", studentB1[1])
print("studentC ikinci notu:", studentC1[3][1])
print(f"{studentA1[0]} {studentA1[1]} {2019-studentA1[2]} yaşında ve not ortalaması {(studentA1[3][0] + studentA1[3][1] + studentA1[3][2])/3}")
print("\n" + 20 * '-' + "\n")

numbers2 = [1, 10, 5, 16, 4, 9, 10]
letters2 = ['a', 'g', 's', 'b', 'y', 'a', 's']
print("min(numbers):", min(numbers2))
print("max(letters):", max(letters2))
numbers2[4] = 40
numbers2.append(49)
numbers2.insert(-1,52)
numbers2.pop()
numbers2.pop(0)
numbers2.remove(52)
numbers2.sort()
numbers2.reverse()
print("Sıralı numbers:", numbers2)
print("\n" + 20 * '-' + "\n")

names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]
index  = names.index('Deniz')
print("Deniz'in indeksi:", index)
names.pop(index)
years.clear()
print("Güncellenmiş isimler:", years)
print("\n" + 20 * '-' + "\n")

markalar = []
for i in range(3):
    marka = input(f"{i+1}. markayı girin: ")
    markalar.append(marka)
print("Girilen markalar:", markalar)
print("\n" + 20 * '-' + "\n")