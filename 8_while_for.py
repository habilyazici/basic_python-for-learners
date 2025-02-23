number=0
while number<=10:
    number = number+1
    print(number)
    if number==5:
        break 
# break direkt döngüden çıkartır ama continue bir döngüyü atlar ve döngüye devam eder.

for x in range(20, 32 , 3):
    print(x)

friends= ['ali', 'mehmet', 'selim', 'osman', 'süleyman']
x=0
while x < len(friends):
    friend = friends[x]
    x= x+1
    if friend == 'selim':
        continue
    print(friend)


for x in friends:
    if x == 'selim':
        continue
    print(x)

message= ''

my_flag= True
while my_flag:
    message= input('quit yazarsanız çıkabilirsiniz! ')
    if message=='quit': 
        my_flag= False 
    else: 
        print(f'{message} kabul edilemez lüten geçerli sözcüğü giriniz.')

list=[]
number2=0
while number2<=10:
    number2 += 1
    if number2 % 2 == 0:
        continue
    list.append(number2)
print(list)

friends= ['ali', 'mehmet', 'selim', 'osman', 'süleyman']
for i, friend in enumerate(friends):
    print(i, friend)

# import random
# xnumber= random.randint(1, 100)
xnumber= 89
num= int(input('lütfen 1 ile 100 arasında bir sayı giriniz: '))
while xnumber != num:
    if num < xnumber:
        print('Bu sayı değil, lütfen daha büyük sayı giriniz. ')
    else:
        print('bu sayı değil, lütfen daha küçük bir sayı giriniz. ')
    num= int(input())
print('tebrikler sayıyı buldunuz')

print('1 den girdiğiniz sayıya kadar olan tüm sayılar toplanacaktır(maximum sayı 1000\'e kadar toplama işlemi yapılır)')
sayi_gir= int(input('lütfen sayıyı giriniz.'))
while True:
    if sayi_gir<0 or sayi_gir >=1000 :
        print('negatif sayı veya 1000 den büyük bir sayı giremezsiniz.')
        sayi_gir= int(input('Tekrar girin'))
    else:
        break
sum= 0
while sayi_gir>0:
    sum+=sayi_gir
    sayi_gir -= 1
print('toplam sayı: ', sum)