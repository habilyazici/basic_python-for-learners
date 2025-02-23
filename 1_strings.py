x = 'selami'
print(x)
x = 20 
print(x)
#tek tırnak işareti, çift tırnak veya parantez içerisinde tek veya çift tırnak işareti pyhton tarafından string olarak algılanmaktadır

name= 'habil yazlılım'
print(len(name))
print(name[0])
print(name[2:7]) # index olarak söylüyor ikinci indexten başlarım diyor yani. indexin bir eksiğine kadar gider
print(name[:5])
print(name[3:])
print(name[-1])
print(name[::-1])

name= 'habil yazlılım'
name2= 'alaSAASskWWWWWdjg'
print(name.title()) # lower upper
print(name2.count('W'))
print(name.find('m'))
print('merhaba dünya'.upper())
# print(dir()) ve print(dir(name)) ile pyhtondaki şuan aktif olan tüm kurallar ve methodları görebilirsin.
# print(help(str))
# print(help(str.lower))
print(dir(name))

my_string = 'carlito\'s day'
my_string2 = "carlito's day"
my_string2 = '''carlito's day'''
print(my_string)
print(my_string2)

name = 'naber '
name2 = 'selam '  
messsage = 'merhaba? ' + name  + name2  
print(messsage)
diğer3= 'merhaba'    ' '  +    name2 + 'buraya geldiğiniz için çok teşekkürler' + ' ' + str(12)
#Ekleme yapbilmek için tüm kavramların aynı türde veri yapısı olması gerekir. 
print(diğer3)

habil = 'hoşgeldilniz'
diğer = f'merhaba habil nasılsın'
messsage2 =  f'merhaba  {habil} nasılsın?'
print(diğer)
print(messsage2)

habil2 = 'hoşgeldiniz'
habil3 = ' ' + 'nasılsınız'
message3 = 'merhaba     {}{} ve dersimizi dinle'
print(message3.format(habil2,habil3))

new_string= 'merhaba {} oyunumuza hoşgeldiniz ilk bonus olarak size {} puan tanımlanmıştır'
print(new_string.format('habil', 43))
print(new_string.replace('ilk', 'first'))
print(new_string.startswith('mer'))
print(new_string.endswith('tır'))

name= 'Habil '
print('my name is ' + name + 'hoşgeldiin')
print('my name is {}'.format(name) )
print(f'my name is {name} dir')