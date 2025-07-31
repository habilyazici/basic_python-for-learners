# Listeler

# --- lists.py ---
message = 'Hello There. My name is Sadık Turan'.split()
# print(message[0])
# my_list = [1,2,3]
# my_list = ['bir',2, True, 5.6]
# print(my_list)
list1 = ['one','two','there']
list2 = ['four','five','six']
numbers = list1 + list2
print(numbers)
print(len(numbers))
print(message[0])
print(numbers[2])
userA = ['Sadık', 36]
userB = ['Çınar', 2]
users = [userA, userB]
print(userA)
print(userB)
print(users)
print(users[0][0])

# --- lists-demo.py ---
arabalar = ['Bmw','Mercedes','Opel','Mazda']
result = len(arabalar)
result = arabalar[0]
result = arabalar[3]
result = arabalar[-1]
# arabalar[-1]= 'Toyota'
result = arabalar
result = 'Mercedes' in arabalar
result = arabalar[-2]
result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]
arabalar[-2:] = ['Toyota','Renault']
result = arabalar
result = arabalar + ['Audi','Nissan']
del arabalar[-1]
result = arabalar
result = arabalar[::-1]
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]
result = studentA[0]
result = studentB[1]
result = studentC[3][1]
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)

# --- list-methods.py ---
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)
val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]
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
print(numbers)
print(letters)
print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count('a'))
numbers.clear()
print(numbers)

# --- list-methods-demo.py ---
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
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)
