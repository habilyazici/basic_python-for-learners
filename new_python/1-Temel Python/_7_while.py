x = 1
while x <= 10:
    if x % 2==1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1
print("\n" + 20 * '-' + "\n")

sayilar = [1, 2, 3, 4, 5]
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1

baslangic = int(input("Başlangıç değerini girin: "))
bitis = int(input("Bitiş değerini girin: "))
i = baslangic
while i <= bitis:
    if i % 2 == 1:
        print(i)
    i += 1
print("\n" + 20 * '-' + "\n")

urunler = []
while True:
    ad = input("Ürün adı (çıkmak için 'q' tuşlayın): ")
    if ad == 'q':
        break
    fiyat = float(input("Ürün fiyatı: "))
    urunler.append({'ad': ad, 'fiyat': fiyat})
for urun in urunler:
    print(f"Ad: {urun['ad']}, Fiyat: {urun['fiyat']}")
print("\n" + 20 * '-' + "\n")

x = 0
result = 0
while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
print(f'toplam: {result}')
print("\n" + 20 * '-' + "\n")