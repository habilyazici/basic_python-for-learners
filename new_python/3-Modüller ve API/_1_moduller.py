# Bir dosya oluşturup onu çağırmak modüldür.
# from math import * Bu yöntemde 'math' adında bir nesne oluşmaz, sadece fonksiyonları doğrudan kullanabilirsin (math.sqrt gibi yazamazsın, sqrt(9) yazarsın).
import math

print(dir(math))
# print(help(math))
print(help(math.factorial))
print(math.sqrt(49))
print(math.factorial(5))
print(math.floor(5.9))
print(math.ceil(5.9))
print("\n" + 20 * '-' + "\n")

from math import factorial, sqrt, ceil
def sqrt(x):
    return 'x :' + str(x)
print(factorial(5))
print(sqrt(9))
print(ceil(9.8))
print("\n" + 20 * '-' + "\n")

import random as random
print(random.random())
print(random.random() * 100)
print(int(random.uniform(10,100)))
print(random.randint(1,100))
print("\n" + 20 * '-' + "\n")

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
print(random.choice(names))
print(random.choice(greeting))
print("\n" + 20 * '-' + "\n")

liste = list(range(10))
random.shuffle(liste)
print(liste)
print(liste[0])
print("\n" + 20 * '-' + "\n")

liste2 = range(100)
result3 = random.sample(liste2, 3)
print(result3)
result4 = random.sample(names, 2)
print(result4)