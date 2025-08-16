# Bir nesnenin elemanlarını tek tek almak için kullanılırlar bellekte tüm elemanları tutmak yerine tek tek tutarlar. Bir list, tuple, set veya dictionary gibi nesneler otomatik olarak __iter__ (iterable) dır dolayısıyla for kullanabiliyoruz. for x in liste(yada başka bir iterable): Python arka planda otomatik olarak iter(liste) çağırır ve her adımda next() ile elemanları alır
liste = [1,2,3,4,5]
iterator = iter(liste)
# böyle yaparak listenin iteratör nesnesini oluşturduk bu sayede nesne next() fonksiyonuyla beraber kullanmaya hazır olur.
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("\n" + 20 * '-' + "\n")

liste2 = [1,2,3,4,5]
iterator = iter(liste2)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
print("\n" + 20 * '-' + "\n")

liste3 = [1,2,3,4,5]
iterator = iter(liste3)
for item in iterator:
    print(item)
print("\n" + 20 * '-' + "\n")

# Bir nesne iterable ise __iter__ metodu vardır ve bu metot bir iterator döner.
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

object = MyNumbers(20,30)

while True:
    try:
        print(next(object))
    except StopIteration:
        break

# myiter = iter(object)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(object))
# for i in myiter:
#     print(i)
print("\n" + 20 * '-' + "\n")


# generator function
def cube():
    for i in range(5):
        yield i ** 3
print(cube())

for i in cube():
    print(i)
print("\n" + 20 * '-' + "\n")

generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)
# print(next(generator))
# print(next(generator))
# print(next(generator))