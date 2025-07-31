# =====================================================
# 1. String Tanımlama ve Temel İşlemler
# =====================================================
name = 'Sadık'
surname = 'Turan'
age = 36
greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'
length = len(greeting)
# print(greeting)
# print(greeting[0])
# print(greeting[3])
# print(greeting[length-1])
# print(greeting[-1])
# print(greeting[3:7])
# print(greeting[3:])
# print(greeting[:16])
print(greeting)
print("greeting[2:40:3]", greeting[2:40:3])
print()

# =====================================================
# 2. String Üzerinde Sık Kullanılan İşlemler ve Sorular
# =====================================================
website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
print("1- course uzunluğu:", result)

length = len(website)
# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]
print("2- website[7:10]:", result)

# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
print("3- website[22:25]:", result)
result = website[length-3:length]
print("3- website son 3 karakter:", result)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
print("4- course ilk 15:", result)
result = course[:15]
print("4- course ilk 15 (alternatif):", result)
result = course[-15:]
print("4- course son 15:", result)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
print("5- course tersten:", result)

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis' 
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 
result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job
print("6- string birleştirme:", result)
result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job) 
print("6- format ile:", result)
result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'
print("6- f-string ile:", result)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
print("7- s:", s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc ' * 3
print("8- abc 3 defa:", result)


# =====================================================
# 3. String Metodları ve Fonksiyonları
# =====================================================
message = 'Hello There. My name is Sadık Turan'
message = message.split()
# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()
# message = message.strip()
# message = message.split()
# message = message.split('.')
# message= '---'.join(message)
# index = message.find('Sadık')
# isFound = message.startswith('H') 
# isFound = message.endswith('n') 
# message = message.replace('Sadık','Çınar')
# message = message.replace('ç','c')
#                  .replace('ö','o')
#                  .replace(' ','-')
message = message.center(50,'*')
print(message)


# =====================================================
# 4. String Metodları ile Soru Çözümleri
# =====================================================
website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()
print("1- strip:", result)
result = ' Hello World '.lstrip()
print("1- lstrip:", result)
result = ' Hello World '.rstrip()
print("1- rstrip:", result)
result = website.lstrip('/:pth')
print("1- website lstrip:", result)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = 'www.sadikturan.com'.strip('w.moc')
print("2- strip sadikturan:", result)

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
print("3- lower:", result)
result = course.upper()
print("3- upper:", result)
result = course.title()
print("3- title:", result)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')
print("4- website 'a' sayısı:", result)
result = website.count('www')
print("4- website 'www' sayısı:", result)
result = website.count('www',0,10)
print("4- website 'www' (0-10):", result)

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result = website.startswith('www')
print("5- startswith www:", result)
result = website.startswith('http')
print("5- startswith http:", result)
result = website.endswith('com')
print("5- endswith com:", result)

# 6-  'website' içinde '.com' ifadesi var mı?
result = website.find('com')
print("6- find com:", result)
result = website.find('com',0,10)
print("6- find com (0-10):", result)
result = course.find('Python')
print("6- course find Python:", result)
result = course.rfind('Python')
print("6- course rfind Python:", result)
result = website.index('com')
print("6- website index com:", result)
result = website.rindex('com')
print("6- website rindex com:", result)

# result = website.rindex('comm') # exception
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()
print("7- course isalpha:", result)
result = 'Hello'.isalpha()
print("7- 'Hello' isalpha:", result)
result = course.isdigit()
print("7- course isdigit:", result)
result = '123'.isdigit()
print("7- '123' isdigit:", result)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50, '*')
print("8- center:", result)
result = 'Contents'.ljust(50, '*')
print("8- ljust:", result)
result = 'Contents'.rjust(50, '*')
print("8- rjust:", result)

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-')
print("9- replace -:", result)
result = course.replace(' ', '-',5)
print("9- replace - (5):", result)
result = course.replace(' ', '')
print("9- replace boşluk:", result)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')
print("10- replace World->There:", result)

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')
print("11- split:", result)
# result = result[2]
result = result[5]
print("11- split 5. eleman:", result)
