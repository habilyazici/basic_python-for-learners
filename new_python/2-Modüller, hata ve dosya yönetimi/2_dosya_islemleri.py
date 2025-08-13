# "w": (Write) yazma modu dosya yoksa oluşturur ve varsa içeriğini siler.
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current Directory:", current_dir)
print(type(current_dir))
file = open(current_dir + "/file1.txt", "w", encoding="utf-8")
file.write("Dosya başarıyla oluşturuldu.\n")
file.close()
print("\n" + 20 * '-' + "\n")

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
file2 = open(current_dir + "/newfile.txt", "a", encoding='utf-8')
file2.write("\nÇınar Turan")
file2.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
try:
    file3 = open(current_dir + "/newfile2.txt", "x", encoding='utf-8')
    file3.write("Bu dosya yeni oluşturuldu.")
    file3.close()
except FileExistsError:
    print("Dosya zaten mevcut.")
finally:
    print("Dosya işlemi tamamlandı.")
print("\n" + 20 * '-' + "\n")

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
file4 = open(current_dir + "/newfile.txt", "r", encoding='utf-8')
print(file4.read())
file4.close()
print("\n" + 20 * '-' + "\n")

# 'r+': Dosyayı hem okumak hem yazmak için açar. Dosya mevcut olmalı, yoksa hata verir.
# imleç dosya başında açılır, seek() kullanabilirsin.
with open(current_dir + "/newfile.txt", "r+", encoding="utf-8") as file5:
    file5.seek(80) # Dosya imlecini 80. bayta getirir
    file5.write("deneme ")

with open(current_dir + "/newfile.txt", "r+", encoding="utf-8") as file6:
    print(file6.read())
print("\n" + 20 * '-' + "\n")

# Sayfa başı ortası ve sonunda güncelleme
with open(current_dir + "/newfile.txt", "a", encoding="utf-8") as file7:
    file7.write("\nFerhat Şirin")

with open(current_dir + "/newfile.txt", "r+", encoding="utf-8") as file8:
    content = file8.read()
    content = "Selime Kars\n" + content
    file8.seek(0)
    file8.write(content)

with open(current_dir + "/newfile.txt", "r+", encoding="utf-8") as file9:
    list = file9.readlines()
    print(list)
    list.insert(4,"dördüncü satır\n")
    file9.seek(0)
    file9.writelines(list)
print("\n" + 20 * '-' + "\n")

with open(current_dir + "/newfile.txt", "r", encoding="utf-8") as file10:
    for i in file10:
        print(i, end="") 
    # end="" ile satır sonu eklenmez end olmazsa boş bir satır ekler. for daha az RAM kullanır.
    print("\n" + 20 * '-' + "\n")

    # Tüm içeriği bir defada okuma
    file10.seek(0) # imleci başa al
    print(file10.read())
    print("\n" + 20 * '-' + "\n")

    # Belirli karakter kadar okuma
    file10.seek(0)
    print(file10.read(5))
    print("\n" + 20 * '-' + "\n")

    # readline() satır satır okur. Her çağrıda bir sonraki satırı okur.
    file10.seek(0)
    print(file10.readline(), end="")
    print(file10.readline(), end="")
    print(file10.readline(), end="")
    print("\n" + 20 * '-' + "\n")

    # Tüm satırları liste olarak okuma
    file10.seek(0)
    print(file10.readlines())

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)



# # "r+": (Read and Write) okuma ve yazma. Dosya konumda yoksa hata verir.
# file = open(current_dir + "/newfile.txt","r+",encoding='utf-8
# # "w+": (Write and Read) yazma ve okuma. Dosya konumda yoksa oluşturur.
# file = open(current_dir + "/newfile.txt","w+",encoding='utf-8