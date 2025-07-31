# String İşlemleri

# --- strings.py ---
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
print(greeting[2:40:3])

# --- strings-demo.py ---
website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
length = len(website)
# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]
# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
result = website[length-3:length]
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
result = course[:15]
result = course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis' 
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 
result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job
result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job) 
result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
print(s)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc ' * 3
print(result)

# --- string-methods.py ---
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

# --- string-methods-demo.py ---
website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()
result = website.lstrip('/:pth')
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = 'www.sadikturan.com'.strip('w.moc')
# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
result = course.upper()
result = course.title()
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')
result = website.count('www')
result = website.count('www',0,10)
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result = website.startswith('www')
result = website.startswith('http')
result = website.endswith('com')
# 6-  'website' içinde '.com' ifadesi var mı?
result = website.find('com')
result = website.find('com',0,10)
result = course.find('Python')
result = course.rfind('Python')
result = website.index('com')
result = website.rindex('com')
# result = website.rindex('comm') # exception
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit()
result = '123'.isdigit()
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50, '*')
result = 'Contents'.ljust(50, '*')
result = 'Contents'.rjust(50, '*')
# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-')
result = course.replace(' ', '-',5)
result = course.replace(' ', '')
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')
# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')
# result = result[2]
result = result[5]
print(result)
