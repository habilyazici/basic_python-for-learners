# "w": (Write) yazma modu dosya yoksa oluşturur ve varsa içeriğini siler.
# os kullanmadan, doğrudan göreli yol ile dosya oluşturma
import os
os.makedirs("../1-Temel Python/2-Modüller, hata ve dosya yönetimi", exist_ok=True)
file = open("../1-Temel Python/2-Modüller, hata ve dosya yönetimi/file1.txt", "w", encoding="utf-8")
file.write("Dosya başarıyla oluşturuldu.\n")
file.close()
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










# # 5_dosya_yazma.py
# # with open("newfile.txt","r+", encoding="utf-8") as file:
# #     file.seek(20)
# #     file.write("deneme")
# # with open("newfile.txt","r+", encoding="utf-8") as file:
# #     print(file.read())
# # ***** Sayfa sonunda güncelleme *****
# # with open("newfile.txt","a", encoding="utf-8") as file:
# #     file.write("\nEmel Turan")
# # ***** Sayfa başında güncelleme *****
# # with open("newfile.txt","r+", encoding="utf-8") as file:
# #     content = file.read()
# #     content = "Efe Turan\n" + content
# #     file.seek(0)
# #     file.write(content)
# # ***** Sayfa ortasında güncelleme *****
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     list = file.readlines()
#     list.insert(1,"Yılmaz Aygün\n")
#     file.seek(0)
#     file.writelines(list)
# with open("newfile.txt","r", encoding="utf-8") as file:
#     print(file.read())

# # 6_dosya_okuma.py
# # try:    
# #     file = open("newfile2.txt","r")
# #     print(file)
# # except FileNotFoundError:
# #     print("dosya okuma hatası")
# # finally:
# #     print("dosya kapandı.")
# #     file.close()
# file = open("newfile.txt","r", encoding = "utf-8")
# # ********** for döngüsü
# # for i in file:
# #     print(i, end="")
# # ********** read() fonksiyonu
# # content1 = file.read()
# # print("içerik 1")
# # print(content1)
# # content2 = file.read()
# # print("içerik 2")
# # print(content2)
# # content = file.read(5)
# # content = file.read(3)
# # content = file.read(3)
# # print(content)
# # ********** readline() fonksiyonu
# # print(file.readline(),end="")
# # print(file.readline(),end="")
# # print(file.readline(),end="")
# # print(file.readline(),end="")
# # print(file.readline(),end="")
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # ********** readlines() fonksiyonu
# # liste = file.readlines()
# # print(liste[0])
# # print(liste[1])
# # print(liste[2])
# file.close()

# # 7_dosya_traversing.py
# with open("newfile.txt","r",encoding="utf-8") as file:
#     content = file.read(10)
#     print(content)
#     file.seek(0)
#     print(file.tell())
#     content2 = file.read(10)
#     print(content2)

