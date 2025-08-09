mylist= ['s','y','others']

if 's' and 'y' in mylist:
    print('listende kötü madde var')
else: 
    print('temizsin')

age = int(input('Lütfen çocuğunuzun yaşını yazınız: '))
if age >= 1 and age<=2:
    print('%80 indirm kazandınız')
elif age<=5:
    print('%70 indirim kazandınız')
elif age<=10:
    print('%60 indirim kazandınız')
else:
    print('Hiç indirim kazanamadınız')

my_condition= []
if my_condition:
    print('koşul doğru')
else:
    print('koşul yanlış')
# False, sıfır, none ve boş veri yapıları için else dönecektir onun haricindeki her şey için if koşulu gerçekleşecektir.

x=1000
y=11
print(f'{x} sayısı {y}\'sayısından büyüktür') if x>y else print(str(x) + ' sayısı ' + str(y) + ' sayısından küçüktür')

number= int(input('lütfen faktöryeli alınmasını istediğiniz sayıyı girin: '))
if number == 0: 
    print('0 sayısının faktöryeli 1 dir')
elif number<0: 
    print('negatif bir sayı girdiniz, negatif bir sayının faktöryeli alınamaz. ')
else: 
    faktöryel= 1
    for x in range(1, number+1):
        faktöryel= faktöryel*x
    print(f'{number} sayısının faktöryeli {faktöryel}\'dir')