"""
Dosya işlemleri ve not uygulaması örnekleri
Birleştirilen dosyalar:
- 4_dosya_olusturma.py
- 5_dosya_yazma.py
- 6_dosya_okuma.py
- 7_dosya_traversing.py
- 8_dosya_islemleri.py
- 9_not_uygulamasi.py
"""

# 4_dosya_olusturma.py
import mod
# result = help(mod)
# result = help(mod.func)
result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.person["age"]
result = mod.func(10)
p = mod.Person()
p.speak()
print(result)

# 5_dosya_yazma.py
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())
# ***** Sayfa sonunda güncelleme *****
# with open("newfile.txt","a", encoding="utf-8") as file:
#     file.write("\nEmel Turan")
# ***** Sayfa başında güncelleme *****
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Turan\n" + content
#     file.seek(0)
#     file.write(content)
# ***** Sayfa ortasında güncelleme *****
with open("newfile.txt","r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(list)
with open("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())

# 6_dosya_okuma.py
# try:    
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()
file = open("newfile.txt","r", encoding = "utf-8")
# ********** for döngüsü
# for i in file:
#     print(i, end="")
# ********** read() fonksiyonu
# content1 = file.read()
# print("içerik 1")
# print(content1)
# content2 = file.read()
# print("içerik 2")
# print(content2)
# content = file.read(5)
# content = file.read(3)
# content = file.read(3)
# print(content)
# ********** readline() fonksiyonu
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# ********** readlines() fonksiyonu
# liste = file.readlines()
# print(liste[0])
# print(liste[1])
# print(liste[2])
file.close()

# 7_dosya_traversing.py
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)

# 8_dosya_islemleri.py
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.
# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 
# file = open("newfile.txt","w")
# file = open("C:/users/sadikturan/desktop/newfile.txt","w")
# file.close()
# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Sadık Turan")
# file.close()
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nÇınar Turan")
# file.write("Çınar Turan\n")
# file.close()
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding='utf-8')
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.

