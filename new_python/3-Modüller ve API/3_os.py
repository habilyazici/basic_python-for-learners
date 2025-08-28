import os
from datetime import datetime

print(dir(os))
print(os.name)
print("Mevcut dizin:", os.getcwd()) # get current working directory
os.chdir('C:\\Users\\habil\\OneDrive\\Belgeler\\')
os.chdir('..')
print("\n" + 20 * '-' + "\n")

os.chdir(r'C:\Users\habil\OneDrive\Belgeler\GitHub\basic-python\new_python\2-Hata ve dosya yönetimi')
with open("newfile.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if i == 4:
            print(line.strip())
            break
print("\n" + 20 * '-' + "\n")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    if not os.path.exists("newdirectory"):
        os.mkdir("newdirectory")
    if not os.path.exists("yenidizin/yenidizin2"):
        os.makedirs("yenidizin/yenidizin2")
    if os.path.exists("newdirectory"):
        if os.path.exists("newdirectory2"):
            os.rmdir("newdirectory")
        else:
            os.rename("newdirectory", "newdirectory2")
    print("Dizinler oluşturuldu.")
except Exception as e:
    print("Hata:", e)
finally:
    os.rmdir("newdirectory2")
    os.removedirs("yenidizin/yenidizin2")
    print("Dizinler temizlendi.")
print("\n" + 20 * '-' + "\n")

print("güncel klasörü listele:", os.listdir())
print("\n" + 20 * '-' + "\n")

newdirectory = os.listdir('C:\\')
for dosyaAdi in newdirectory:
    if dosyaAdi.endswith('.txt') or dosyaAdi.endswith('.sys') or dosyaAdi.endswith('Files'):
        print(dosyaAdi)
print("\n" + 20 * '-' + "\n")

result = os.stat("3_os.py")
print(result)
result1 = result.st_size / 1024
result2 = datetime.fromtimestamp(result.st_ctime)
result3 = datetime.fromtimestamp(result.st_atime)
result4 = datetime.fromtimestamp(result.st_mtime)
print("Dosya boyutu (KB): ", result1)
print("Oluşturulma tarihi: ", result2)
print("Son erişilme tarihi: ", result3)
print("Değiştirilme tarihi: ", result4)
print("\n" + 20 * '-' + "\n")

# os.system("start chrome")
# os.system(r"start c:\Users")
# os.system(r"start C:\Users\habil\AppData\Roaming\Spotify\Spotify.exe")
# os.system(f"notepad.exe {yol}")

dosyaYolu = os.path.abspath(__file__)
print("Dosya yolu:", dosyaYolu)
this_directory = os.path.dirname(os.path.abspath(__file__))
print("Dosyanın klasörü:", this_directory)
print("3_os1.py var mı   ", os.path.exists("3_os1.py"))
print("bahsedilen klasör var mı    ", os.path.exists(this_directory))
print("saadece klasör var mı   ", os.path.isdir(this_directory))
print("saadece dosya var mı    ", os.path.isfile("3_os.py"))
print("\n" + 20 * '-')

# join ve split herhangi bir dosya ve klasörün yolunu birleştirmek için tasarlanmıştır.
print(os.path.join("C:\\", "deneme", "deneme1", "join.py"))
split_result = os.path.split("C:\\deneme\\deneme1\\join.py")
print(split_result)
print(type(split_result))
print("Klasör yolu:", split_result[0])
print("Dosya adı:", split_result[1])

splitext_result = os.path.splitext("3_os.py")
print(splitext_result)
print("Dosya adı:", splitext_result[0])
print("Dosya uzantısı:", splitext_result[1])