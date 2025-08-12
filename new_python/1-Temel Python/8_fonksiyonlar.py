def total(num1, num2):
    return num1 + num2
result = total(10,20)
print(result)

def sayHello(name = 'user'):
    return 'Hello '+ name
msg = sayHello("Çınar")
print(msg)
print("\n" + 20 * '-' + "\n")

def yasHesapla(dogumYili):
    return 2019 - dogumYili
ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)
print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'{isim} için emekliliğe {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz')
EmekliligeKacYilKaldi(1983, 'Ali')
print("\n" + 20 * '-' + "\n")

# *args ve **kwargs kullanımı
def add(*params):
    print(type(params))
    total = 0
    for x in params:
        total += x
    return total
print(add(10, 20, 50))
print(add(10, 20, 30, 50, 60, 10, 20))
print("\n" + 20 * '-' + "\n")

def displayUser(**args):
    print(args)
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayUser(name= 'Ada', age = 12, city = 'kocaeli', phone = '123132')
displayUser(name= 'Yiğit', age = 14, city = 'ankara', phone = '123132', email= 'yigit@gmail.com')
print("\n" + 20 * '-' + "\n")

def myFunc(a, b, c, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("args (tuple):", args)
    print("kwargs (dict):", kwargs)
myFunc(1, 2, 3, 4, 5, 6, x=10, y=20, name='mehmet', age=5)
print("\n" + 20 * '-' + "\n")

def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste
print(listeyeCevir(10,20,30,'Merhaba'))
print("\n" + 20 * '-' + "\n")

def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, int(sayi**0.5) + 1):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))
asalSayilariBul(sayi1, sayi2)

def greeting(name):
    return f'hello {name}'
print(greeting('ali'))
del greeting
print("\n" + 20 * '-' + "\n")

global_x = 'global x'
def function():
    global_x = "Yeni global x"
    print(global_x)
function()
print(global_x)

name = 'Çınar'
def changeName(new_name):
    global name
    name = new_name
    print(name)
changeName('Ada')
print(name)