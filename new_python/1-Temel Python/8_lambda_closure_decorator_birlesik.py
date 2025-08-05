# Lambda, Closure, Decorator ve List Methods

# Closure örnekleri
# def usalma(number):
#     def inner(power):
#         return number ** power
#     return inner
# two = usalma(2)
# three = usalma(3)
# print(two(3))
# print(three(4))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner
# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

# Lambda ve map örnekleri
# def square(num): return num ** 2
# square =  lambda num: num ** 2
numbers = [1,3,5,9,10,4]
# result = list(map(lambda num: num ** 2, numbers))
# result = list(map(square, numbers))
# result = square(3)
# for item in map(square, numbers):
#     print(item)
# def check_even(num): return num%2==0
check_even = lambda num: num%2==0
result = check_even(numbers[2])
print(result)

# Decorator örnekleri
import math
import time
def calculate_time(func):
    def inner(*args,**kwargs):        
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)        
        finish = time.time()
        print("fonksiyon "+func.__name__ +" " + str(finish-start) + " saniye sürdü.")
    return inner
@calculate_time
def usalma(a,b):
    print(math.pow(a,b))   
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
@calculate_time
def toplama(a,b):
    print(a+b)
usalma(2,3)
faktoriyel(4)
toplama(10,20)

# List methods
list = [1,2,3]
list.append(4)
list.pop()
print(type(list))
print(list)
myString = 'Hello'
print(myString.upper())
print(type(myString))
