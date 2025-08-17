import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def not_hesapla(satir):
    satir = satir[:-1] # satır sonundaki \n yi almıyor
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')
    try:
        not1 = int(notlar[0])
        not2 = int(notlar[1])
        not3 = int(notlar[2])
    except (ValueError, IndexError):
        return ogrenciAdi + ": Notları girerken bir sorun oluştu\n"
    ortalama = (not1+not2+not3)/3
    if ortalama>=90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=85 and ortalama<=89:
        harf = "BA"
    elif ortalama>=80 and ortalama<=84:
        harf = "BB"
    elif ortalama>=75 and ortalama<=79:
        harf = "CB"
    elif ortalama>=70 and ortalama<=74:
        harf = "CC"
    elif ortalama>=65 and ortalama<=69:
        harf = "DC"
    elif ortalama>=60 and ortalama<=64:
        harf = "DD"
    elif ortalama>=50 and ortalama<=59:
        harf = "FD"
    else:
        harf = "FF"
    return ogrenciAdi + ": " + harf + "\n"

def ortalamalari_oku():
    try:
        with open(current_dir + "/sonuclar.txt", "r", encoding="utf-8") as file:
            contents = file.read()
            if contents.strip() == "": # sağdan soldan dosyadaki boşukları silince hiç veri yoksa 
                print("Daha not girilmedi.")
            else:
                print(contents, end="")
    except FileNotFoundError:
        print("sonuclar.txt dosyası bulunamadı!")

def not_gir():
    ad = input('Öğrenci adı: ').capitalize()
    soyad = input('Öğrenci soyad: ').capitalize()
    while True:
        try:
            not1 = int(input('not 1: '))
            not2 = int(input('not 2: '))
            not3 = int(input('not 3: '))
            break
        except ValueError:
            print("Notlar sayı olmalı!")
    try:
        with open(current_dir + "/sinav_notlari.txt", "a", encoding="utf-8") as file:
            file.write(ad + ' ' + soyad + ':' + str(not1) + ',' + str(not2) + ',' + str(not3)+ '\n') # write() methodu sadece str() türleri kabul eder.
    except Exception:
        print("dosya bulunamadı")
    notlari_kayitet()

def notlari_kayitet():
    with open(current_dir + "/sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
        with open(current_dir + "/sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

print("\nHoşgeldiniz!!")
while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Çıkış\n')
    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == "3":
        break
    else:
        print("hatalı işlem girdiniz\n")