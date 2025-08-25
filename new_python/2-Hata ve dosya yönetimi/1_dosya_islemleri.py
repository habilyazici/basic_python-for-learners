print("\n" + 20 * '-' + "\n")
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current Directory: ", current_dir)
print(type(current_dir))
print("şuanki dizin code dizini: ", os.getcwd())
os.chdir(current_dir)
print("şuanki dizin yeni dizin: ", os.getcwd())

# "w": (Write) yazma modu dosya yoksa oluşturur ve varsa içeriğini siler.
file = open("file1.txt", "w", encoding="utf-8")
file.write("Dosya başarıyla oluşturuldu.\n")
# file.read() dosyayı yazma modunda açtığımız için içeriği okuyamaz.
file.close()
print("\n" + 20 * '-' + "\n")

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
file2 = open("newfile.txt", "a", encoding='utf-8')
file2.write("\nÇınar Turan")
file2.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
try:
    file3 = open("file1.txt", "x", encoding='utf-8')
    file3.write("Bu dosya yeni oluşturuldu.")
    file3.close()
except FileExistsError:
    print("Dosya zaten mevcut.")
finally:
    print("Dosya işlemi tamamlandı.")
print("\n" + 20 * '-' + "\n")

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
with open("newfile.txt", encoding='utf-8') as file4:
    print(file4.read())
print("\n" + 20 * '-' + "\n")

# 'r+': Dosyayı hem okumak hem yazmak için açar. Dosya mevcut olmalı, imleç baştadır.
# "w+": Aynısı ek olarak, dosya konumda yoksa oluşturur. Varsa içeriği siler
with open("newfile.txt", "r+", encoding="utf-8") as file5:
    file5.seek(80)
    file5.write("deneme ")

with open("newfile.txt", "a", encoding="utf-8") as file7:
    file7.write("\nFerhat Şirin")

with open("newfile.txt", "r+", encoding="utf-8") as file8:
    content = file8.read()
    content = "Selime Kars\n" + content
    file8.seek(0)
    file8.write(content)

with open("newfile.txt", "r+", encoding="utf-8") as file9:
    list = file9.readlines()
    print(list)
    list.insert(4,"dördüncü satır\n")
    file9.seek(0)
    file9.writelines(list)
print("\n" + 20 * '-' + "\n")

with open("newfile.txt", "r", encoding="utf-8") as file10:
    for i in file10:
        print(i, end="-") 
    # end="" olmalı böylece satır sonu eklenmez end olmazsa boş bir satır ekler. for daha az RAM için kullanılır.
    print("\n" + 20 * '-' + "\n")

    file10.seek(0)
    print(file10.read())
    print("\n" + 20 * '-' + "\n")

    file10.seek(0)
    print(file10.read(5))
    print("\n" + 20 * '-' + "\n")

    # veriler iterabledır, readline() satır satır okur. Her çağrıda bir sonraki satırı okur.
    file10.seek(0)
    print(file10.readline(), end="")
    print(file10.readline(), end="")
    print(file10.readline(), end="")
    print("\n" + 20 * '-' + "\n")

    file10.seek(0)
    while True:
        satir = file10.readline()
        if not satir:
            break
        print(satir, end="")
    print("\n" + 20 * '-' + "\n")

    file10.seek(0)
    print(file10.readlines())
    print("\n" + 20 * '-' + "\n")

with open("newfile.txt", "r", encoding="utf-8") as file11:
    print(file11.read(10))
    print(file11.read(8))
    print(file11.tell())
    file11.seek(0)
    print(file11.read(18))
    # \n bir byte okunuyor