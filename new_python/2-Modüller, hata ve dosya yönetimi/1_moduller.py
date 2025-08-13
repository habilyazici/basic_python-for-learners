# bir dosya oluşturup onu çağırmakta bir modüldür.
# from math import *   # bu yöntemde math adında nesne yoktur o yüzden kullanamazsın.
# import math as islem
import math

print(dir(math))
# print(help(math))
print(help(math.factorial))
print(math.sqrt(49))
print(math.factorial(5))
print(math.floor(5.9))
print(math.ceil(5.9))
# print(islem.factorial(5))
print("\n" + 20 * '-' + "\n")

from math import factorial, sqrt, ceil
def sqrt(x):
    return 'x :'+ str(x)
value1 = factorial(5)
value2 = sqrt(9)
value3 = ceil(9.8)
print(value1)
print(value2)
print(value3)
print("\n" + 20 * '-' + "\n")

import random as random
print(random.random()) # 0.0 - 1.0
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
