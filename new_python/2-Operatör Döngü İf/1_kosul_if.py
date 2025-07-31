# =====================================================
# Koşul İfadeleri ve if-else
# =====================================================

# Basit if-else örneği
username = 'sadikturan'
password = '1234'
if (username == 'sadikturan'):
    if (password == '12345'):
        print('Hoş geldiniz')
    else:
        print('parola yanlış')
else:
    print('username yanlış')

# if-elif örneği
num = int(input('sayı: '))
if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')

# Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumu
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim = input('isminiz: ')
yas = int(input('yaşınız: '))
egitim = input('eğitim: ')
if (yas>=18):
    if (egitim=='lise' or egitim=='üniversite'):
        print(f'{isim} ehliyet alabilirsin.')
    else:
        print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
else:
    print(f'{isim} ehliyet alamazsın yaşın tutmuyor.')

# Not ortalaması ve aralık kontrolü

yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sözlü: '))
ortalama = (yazili1 + yazili2 + sozlu)/3
if (ortalama>=0) and (ortalama<25):
    print(f'ortalamanız: {ortalama} notunuz: 0')
elif (ortalama >= 25 ) and (ortalama<45):
    print(f'ortalamanız: {ortalama} notunuz: 1')
elif (ortalama >= 45 ) and (ortalama<55):
    print(f'ortalamanız: {ortalama} notunuz: 2')
elif (ortalama >= 55 ) and (ortalama<70):
    print(f'ortalamanız: {ortalama} notunuz: 3')
elif (ortalama >= 70 ) and (ortalama<85):
    print(f'ortalamanız: {ortalama} notunuz: 4')
elif (ortalama >= 85 ) and (ortalama<=100):
    print(f'ortalamanız: {ortalama} notunuz: 5')
else:
    print('yanlış bilgi girdiniz.')

# 0-100 arası kontrol

sayi = float(input('sayı: '))
if (sayi > 0) and (sayi<=100):
    print('sayı 0-100 arasında.')
else:
    print('sayı 0-100 arasında değildir.')
