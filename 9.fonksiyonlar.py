# fonksiyonlar builtin ve custom(özel fonksiyonlar) olarak ikiye ayrılır.
#builtin func: sum, print, len gibi, 'built in functions in python' google'le veya builtin.py dosyasına bak
def merhaba():
    x= 'işlem...'
    print('merhaba dünya hoşgeldiniz')
merhaba()

def func33():
    return 3+3
def func55():
    print(5+5)
print(func33())
func55()

def my_function(username= 'ANAKONDA', lastname='' ):
    print(f'merhaba {username} geçen adın bu muydu {lastname}')
my_function('serhat', 'aslıhan')

üs_alma_islemi= lambda rakam, rakam2, rakam3: rakam**6 + rakam2*2 + rakam3**4
print(üs_alma_islemi(4, 3 , 4))

kimlik1= int(input('lütfen kimlik no giriniz'))
kimlik2= input('lütfen ad giriniz')
kimlik3= input('lütfen soyad giriniz')
kimlik4= int(input('lütfen doğum tarihi giriniz'))
def müsteriEkle(kimlik1, kimlik2, kimlik3, kimlik4):
    return 'kimlik bilgileri sırasıyla: ' , kimlik1, kimlik2, kimlik3, kimlik4
print(müsteriEkle(kimlik1, kimlik2, kimlik3, kimlik4))

def sayiCarpimMekanizmasi():
    print('Girdiğiniz birden çok sayının hepsini çarpabileceğiniz mekanizmaya hoşgeldiniz.')
    liste = []
    while True:
        y = str(input('çıkmak için quit yazabilirsiniz veya sayı girebilirsiniz'))
        if y == 'quit':
            break
        else:
            liste.append(float(y))
    if len(liste) == 0:
        print('hiçbir sayı girmediğiniz için çarpım işlemi gerçekleşmedi')
    else:
        carpim= 1
        for x in liste:
            carpim *= x
        print(carpim)

        # carpim = 1
        # i = 0
        # while i < len(liste):
        #     carpim *= liste[i]
        #     i += 1
        # print(carpim)
sayiCarpimMekanizmasi()

a = int(input('faktöryeli alınması istediğiniz sayıyı giriniz.'))
def faktoriyel(a):
    if a == 0:
        return 1     #sayı olan bir bu 
    else:
        return a*faktoriyel(a-1)
print(faktoriyel(a))

#HESAP MAKİNESİ
def topla(x,y):
    return x+y
def cikar(x,y):
    return x-y
def carp(x,y):
    return x*y
def bol(x,y):
    while y==0:
        print('bir sayı sıfıra bölünemez!')
        y = int(input('Yeni sayıyı giriniz:'))
    return x/y

islem= input('yapmak istediğiniz işlem ne(4 işlemden biri) veya çıkmak için quit yazınız: ').lower()
list= ['çarpma', 'çarp', 'çıkarma', 'çıkar', 'toplama', 'topla', 'böl', 'bölme', 'quit']
while islem not in list:
    print('belirttiğiniz işlem mevcut değil')
    islem= input('yapmak istediğiniz işlem ne(4 işlemden biri): ').lower()
if islem == 'quit':
    print('Çıkış yapıldı')
else:
    x= int(input('lütfen ilk değeri giriniz: '))
    y= int(input('lütfen ikinci değeri giriniz: '))

    if islem == 'toplama' or islem ==  'topla':
        print(topla(x, y))
    elif islem == 'çıkar' or islem ==  'çıkarma':
        print(cikar(x, y))
    elif islem == 'çarpma' or islem == 'çarp':
        print(carp(x, y))
    elif islem == 'bölme' or islem == 'böl':
        print(bol(x, y))