print("\n" + 20 * '-' + "\n")
first_name = 'Sadık'
last_name = 'Turan'
person_age = 36
greeting = 'My name is ' + first_name + ' ' + last_name + ' and \nI am ' + str(person_age) + ' years old'
print("greeting:", greeting)
print("greeting[2:40:3]", greeting[2:40:3])
print("greeting[0]", greeting[0])
print("greeting[length-1]", greeting[len(greeting)-1])
print("greeting[-1]", greeting[-1])
print("greeting[3:]", greeting[3:])
print("greeting[:16]", greeting[:16])
print("\n" + 20 * '-' + "\n")

website1 = "http://www.facebook.com"
course1  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (100 saat)"
print("2- website[7:10]:", website1[7:10])
print("3- website son 3 karakter:", website1[len(website1)-3:len(website1)])
print("4- course ilk 15:", course1[0:15]) # course1[:15]
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

person_name = 'Çınar'
person_surname = 'Turan'
person_age = 36
print("My name is {} {} and I'm {} years old.".format(person_name, person_surname, person_age))
print('My name is {1} {0}'.format(person_name, person_surname))
print('My name is {s} {n}'.format(n=person_name, s=person_surname))
result_format = 200 / 700
print('the result is {r:1.7}'.format(r=result_format))
print("\n" + 20 * '-' + "\n")

value_x = 5
value_y = 25
value_x = value_y
value_y = 10
print("Value types (x, y):", value_x, value_y)

list_a = ["apple","banana"]
list_b = ["apple","banana"]
list_a = list_b
list_b[0] = "grape"
print("Reference types (a, b):", list_a, list_b)

str_x = '10'
str_y = '20'
str_x = str_y
str_y = '5'
print("str_x-y:", str_x, str_y)
print("\n" + 20 * '-' + "\n")

message1 = '   Hello There. My name is Habil Yazıcı'
print("upper:", message1.upper()) # .lower(), .title(), .capitalize()
print("strip:", message1.strip())
print("split:", message1.split('.'))
print("join:", '---'.join(message1.split()))
print("find:", message1.find('Habil'))
print("startswith:", message1.startswith('H'))
print("endswith:", message1.endswith('n'))
print("\n" + 20 * '-' + "\n")

website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

print("9- replace - (5 adet):", course.replace(' ', '-', 5))
print("9- replace boşluk:", course.replace(' ', ''))
result = course.split(' ')
print("11- split:", result)
print("11- split 5. eleman:", result[5])
print("replace:", message1.replace('ç','c').replace('ı','i').replace(' ','-'))
print("\n" + 20 * '-' + "\n")

print("1- lstrip:", '   Hello World   '.lstrip())
print("1- rstrip:", '   Hello World   '.rstrip())
print("1- lstrip website :", website.lstrip('/:pth'))
print("2- strip:", 'www.sadikturan.com'.strip('w.moca'))
print("4- website 'a' sayısı:", website.count('a'))
print("4- website 'www' sayısı:", website.count('www'))
print("4- website 'www' (0-10) arasında:", website.count('www',0,10))
print("\n" + 20 * '-' + "\n")

print("6- find com (0-10):", website.find('com',0,10))
print("6- course lfind Python:", course.find('Python'))
print("6- course rfind Python:", course.rfind('Python'))
print("6- website index com:", website.index('com'))
print("6- website rindex com:", website.rindex('com'))
# rindex sağdan gelir ve bulursa onun indexini söyler 'com' bir tane var.
# find aranan ifade bulunamazsa -1 döner, index ise aranan ifade bulunamazsa exception fırlatır.
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