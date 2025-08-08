number1 = 20
print("number1:", number1)
number1 += 30
print("number1 güncellendi (30 eklendi):", number1)
number1 = 20
print("number1 tekrar güncellendi:", number1)
number1 += 30
print("number1 tekrar güncellendi (30 eklendi):", number1)
print("\n" + 20 * '-' + "\n")

age = 20
AGE = 30
_age = 40
print("age (küçük harfli):", age)
print("AGE (büyük harfli):", AGE)
print("_age (alt çizgili):", _age)
print("\n" + 20 * '-' + "\n")
x, y, name, isStudent = (1, 2.3, "Çınar", True)

a = '10'
b = '20'
print("a+b (string):", a+b)
firstName = "Sadık"
lastName = " Turan"
print("Ad Soyad:", firstName + lastName)
print("\n" + 20 * '-' + "\n")

x_input1 = input('1.sayı: ')
y_input1 = input('2.sayı: ')
print(type(x_input1))
toplam_input1 = int(x_input1) + int(y_input1)
print("Toplam:", toplam_input1)

x4, y4, name4, isOnline4 = 5, 2.5, 'Çınar', True
print(type(x4), type(y4), type(name4), type(isOnline4))
print(float(x4))
print(int(y4))
print(str(x4) + str(y4))
print(str(isOnline4))
isOnline5 = False
print("isOnline (int):", int(isOnline5))
print("\n" + 20 * '-' + "\n")

pi = 3.14
r = float(input("Yarı çapı girin: "))
alan = pi * (r ** 2)
print("Alan tipi:", type(alan)) # floatla intigeri çarparsan float olur
cevre = 2 * pi * r
print("Dairenin alanı:", alan, "Çevresi:", cevre)