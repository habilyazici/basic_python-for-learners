import os
from datetime import datetime

print(dir(os))
print(os.name)
print("\n" + 20 * '-' + "\n")

print("Mevcut dizin:", os.getcwd()) # get current working directory
# C:\Users\habil\OneDrive\Belgeler\GitHub\ şeklinde gider normalde dizinler 
os.chdir('C:\\Users\\habil\\OneDrive\\Belgeler\\')
os.chdir('..')
print("Mevcut dizin:", os.getcwd())
print("\n" + 20 * '-' + "\n")

os.chdir('C:\\Users\\habil\\OneDrive\\Belgeler\\GitHub\\basic-python\\new_python\\2-Hata ve dosya yönetimi')
with open("newfile.txt", "r+", encoding="utf-8") as f:
    f.seek(0)
    okundu = f.read()
    print(okundu)
print("\n" + 20 * '-' + "\n")

# dosya oluşturma
os.chdir('C:\\Users\\habil\\OneDrive\\Belgeler\\GitHub\\basic-python\\new_python\\3-Advanced Python Modülleri')
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
 
# listeleme
print("güncel klasör:", os.listdir())
print("\n" + 20 * '-' + "\n")

newdirectory = os.listdir('C:\\')
for dosyaAdi in newdirectory:
    print(dosyaAdi)
print("\n" + 20 * '-' + "\n")

for dosyaAdi in newdirectory:
    if dosyaAdi.endswith('.txt') or dosyaAdi.endswith('.py') or dosyaAdi.endswith('Files'):
        print(dosyaAdi)
print("\n" + 20 * '-' + "\n")

print(os.getcwd())
os.chdir('..')
os.chdir('2-Hata ve dosya yönetimi')
print(os.getcwd())
result = os.stat("1_dosya_islemleri.py")
print(result)
print("\n" + 20 * '-' + "\n")

result1 = result.st_size/1024
result2 = datetime.fromtimestamp(result.st_ctime)
result3 = datetime.fromtimestamp(result.st_atime)
result4 = datetime.fromtimestamp(result.st_mtime)
print("Dosya boyutu (KB):", result1)
print("Oluşturulma tarihi:", result2)
print("Son erişilme tarihi:", result3)
print("Değiştirilme tarihi:", result4)
print("\n" + 20 * '-' + "\n")

# os.system("start chrome")
yol = os.path.join("C:\\Users\\habil", "OneDrive", "Belgeler", "GitHub", "basic-python", "new_python", "2-Hata ve dosya yönetimi", "file1.txt")
print("Dosya yolu:", yol) # pythonda iki ters eğik çizgi kullanılır çünkü tek ters eğik çizgi özel bir karakterdir kaçış karakteridir.
os.system(f"notepad.exe {yol}")
print("\n" + 20 * '-' + "\n")

os.chdir('..')
os.chdir('3-Advanced Python Modülleri')
print(os.getcwd())

base_dir = r"C:/Users/habil/OneDrive/Belgeler/GitHub/basic-python/new_python/3-Advanced Python Modülleri"
file_py = os.path.join(base_dir, "3_os.py")
file_py1 = os.path.join(base_dir, "3_os1.py")

print(os.path.abspath(file_py))
print(os.path.dirname(file_py))
print(os.path.dirname(os.path.abspath(file_py)))
print(os.path.exists(file_py1))
print(os.path.exists(base_dir))
print(os.path.isdir(base_dir))
print(os.path.isfile(file_py))

print(os.path.join("C:\\", "deneme", "deneme1"))
split_result = os.path.split("C:\\deneme")
print(split_result)
print("Klasör yolu:", split_result[0])
print("Klasör adı:", split_result[1])

splitext_result = os.path.splitext(file_py)
print(splitext_result)
print("Dosya adı:", splitext_result[0])
print("Dosya uzantısı:", splitext_result[1])

