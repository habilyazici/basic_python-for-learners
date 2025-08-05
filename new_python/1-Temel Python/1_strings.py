first_name = 'Sadık'
last_name = 'Turan'
person_age = 36
greeting = 'My name is ' + first_name + ' ' + last_name + ' and \nI am ' + str(person_age) + ' years old'
print("greeting:", greeting)
print("greeting[2:40:3]", greeting[2:40:3])
print("greeting[0]", greeting[0])
print("greeting[length-1]", greeting[len(greeting)-1])
print("greeting[-1]", greeting[-1])
print("greeting[3:7]", greeting[3:6])
print("greeting[3:]", greeting[3:])
print("greeting[:16]", greeting[:16])
print("\n" + 20 * '-' + "\n")

website1 = "http://www.facebook.com"
course1  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (100 saat)"
print("1- course uzunluğu:", len(course1))
# 2- 'website' içinden www karakterlerinin alınması 
print("2- website[7:10]:", website1[7:10])
print("3- website son 3 karakter:", website1[len(website1)-3:len(website1)])
print("4- course ilk 15:", course1[0:15])
print("4- course ilk 15 (alternatif):", course1[:15])
print("4- course son 15:", course1[-15:])
print("5- course tersten:", course1[::-1] )
print("\n" + 20 * '-' + "\n")

name2, surname2, age2, job2 = 'Bora','Yılmaz', 32, 'mühendis' 
result9 = "Benim adım "+ name2+ " " + surname2+ ", Yaşım "+ str(age2) + " ve mesleğim "+ job2
print("6- string birleştirme:", result9)
result10 = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name2,surname2,age2,job2) 
print("6- format ile:", result10)
result11 = f'Benim adım {name2} {surname2}, Yaşım {age2} ve "mesleğim" {job2}.'
print("6- f-string ile:", result11)
print("\n" + 20 * '-' + "\n")

s1 = 'Hello world'
s1 = s1[0:6] + 'W'+ s1[-4:]
print("7- s:", s1)
print("8- abc 3 defa yazdır:", 'abc ' * 3)
print("\n" + 20 * '-' + "\n")

# --- 6_format_reference.py'den eklenen örnekler ---
person_name = 'Çınar'
person_surname = 'Turan'
person_age = 36
print('My name is {} {}'.format(person_name, person_surname))
print('My name is {1} {0}'.format(person_name, person_surname))
print('My name is {s} {n}'.format(n=person_name, s=person_surname))
print("My name is {} {} and I'm {} years old.".format(person_name, person_surname, person_age))
print("My name is {} {} and I'm {} years old.".format(person_name, person_name, person_name))
result_format = 200 / 700
print('the result is {r:1.4}'.format(r=result_format))
print(f"My name is {person_name} {person_surname} and I'm {person_age} years old.")
print()

# value types => string, number
value_x = 5
value_y = 25
value_x = value_y
value_y = 10
print("Value types (x, y):", value_x, value_y)
# reference types => list
list_a = ["apple","banana"]
list_b = ["apple","banana"]
list_a = list_b
list_b[0] = "grape"
print("Reference types (a, b):", list_a, list_b)
print()

# Stringlerde değer tipi davranışı
str_x = '10'
str_y = '20'
str_x = str_y
str_y = '5'
print("str_x:", str_x)
print("str_y:", str_y)

# Listelerde referans tipi davranışı
list_x = ["apple", "banana"]
list_y = ["apple", "banana"]
list_y = list_x
print("list_x is list_y before change:", list_x is list_y)
list_x[0] = 'grape'
print("list_x is list_y after change:", list_x is list_y)
print("list_x:", list_x)
print("list_y:", list_y)

message1 = '   Hello There. My name is Sadık Turan'
print(message1.upper()) # .lower(), .title(), .capitalize()
print(message1.strip())
print(message1.split())
print(message1.split('.'))
print('---'.join(message1.split()))
print(message1.find('Sadık'))
print(message1.startswith('H'))
print(message1.endswith('n'))
print(message1.replace('Sadık','Çınar'))
print(message1.replace('ç','c').replace('ö','o').replace(' ','-'))
print("\n" + 20 * '-' + "\n")

website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
print("1- strip:", '   Hello World   '.strip())
print("1- lstrip:", '   Hello World   '.lstrip())
print("1- rstrip:", '   Hello World   '.rstrip())
print("1- lstrip website :", website.lstrip('/:pth')) 
print("2- strip sadikturan:", 'www.sadikturan.com'.strip('w.moc'))
print("4- website 'a' sayısı:", website.count('a'))
print("4- website 'www' sayısı:", website.count('www'))
print("4- website 'www' (0-10) arasında:", website.count('www',0,10))
print("\n" + 20 * '-' + "\n")

print("6- find com:", website.find('com'))
print("6- find com (0-10):", website.find('com',0,10))
print("6- course find Python:", course.find('Python'))
print("6- course rfind Python:", course.rfind('Python'))
print("6- website index com:", website.index('com'))
print("6- website rindex com:", website.rindex('com'))
# find aranan ifade bulunamazsa -1 döner, index ise aranan ifade bulunamazsa exception fırlatır.
# print(" hata fırlatan index: ", website.index('comm')) # exception
print("\n" + 20 * '-' + "\n")

print("7- course isalpha:", course.isalpha())
print("7- 'Hello' isalpha:", 'Hello'.isalpha())
print("7- course isdigit:", course.isdigit())
print("7- '123' isdigit:", '123'.isdigit())
# isaplhada: sadece harflerden oluşuyorsa True, isdigitte: sadece rakamlardan oluşuyorsa True
print("8- center:", 'Contents'.center(50, '*'))
print("8- ljust:", 'Contents'.ljust(50, '*'))
print("8- rjust:", 'Contents'.rjust(50, '*'))
print("\n" + 20 * '-' + "\n")

print("9- replace -:", course.replace(' ', '-'))
print("9- replace - (5 adet):", course.replace(' ', '-', 5))
print("9- replace boşluk:", course.replace(' ', ''))
print("10- replace World->There:", 'Hello World'.replace('World','There'))
result = course.split(' ')
print("11- split:", result)
print("11- split 5. eleman:", result[5])
