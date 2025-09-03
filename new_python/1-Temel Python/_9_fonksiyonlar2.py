# Closure Fonksiyonlar
def usalma(number):
    def inner(power):
        return number ** power
    return inner
    # fonksiyonunun kendisini çağırıyor fonksiyonu döndürmüyor.
two = usalma(2)
print(two(3))

def usalma(number):
    def inner(power):
        return number ** power
    return inner
print(usalma(2)(3))
print("\n" + 20 * '-' + "\n")

def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return f"'{role}' rolü '{page}' sayfasına ulaşabilir."
        else:
            return f"'{role}' rolü '{page}' sayfasına ulaşamaz."
    return inner
user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))
print("\n" + 20 * '-' + "\n")

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

topla = islem("toplama")
print(topla(1, 2, 3)) 
carp = islem("carpma")
print(carp(2, 3, 4, 5, 6))
print("\n" + 20 * '-' + "\n")

# Decorator Fonksiyonları
import math
import time

def toplama(a, b):
    start = time.time()
    time.sleep(1)
    print(a + b)
    finish = time.time()
    print("fonksiyon toplama", str(finish - start), "saniye sürdü.")
toplama(10, 20)
print("\n" + 20 * '-' + "\n")

def calculate_time(func):
    def inner(*args,**kwargs):
        # burda *args ve **kwargs kullanırsak kapsadığımız fonksiyon istediği kadar parametre ve istediği parametreyi alabilir dict, string, int, float vs.
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(f"fonksiyon {func.__name__} {finish-start} saniye sürdü.")
    return inner

@calculate_time
def usalma(a, b):
    print(math.pow(a, b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2, 3)
faktoriyel(4)
print("\n" + 20 * '-' + "\n")

# Lambda Fonksiyonları ve map Kullanımı
def square(num): return num ** 2
print("square(5):", square(5))

square2 = lambda num: num ** 2
print("square2(5):", square2(50))

numbers = [1, 3, 5, 9, 10, 4]
result = list(map(lambda num: num ** 2, numbers))
print("map ile bir açık fonksiyon ve listenin işlenmesi:", result)

result2 = list(map(square, numbers))
print("map ile bir kapalı fonksiyon ve listenin işlenmesi:", result2)
# burda veriler herhangi bir iterable veri olabilir: liste, tuple, set, string, dict, range
for item in map(square, numbers):
    print(item)