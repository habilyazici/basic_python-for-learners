"""
Modül, matematik ve random örnekleri
Birleştirilen dosyalar:
- 1_modul_nedir.py
- 2_math_modulu.py
- 3_random_modulu.py
"""

# 1_modul_nedir.py
'''
   modül hakkında bilgilendirme 
'''
print('modül eklendi')
number = 10
numbers = [1,2,3]
person = {
    "name": "Ali",
    "age":"25",
    "city":"istanbul"
}
def func(x):
    '''
        fonksiyon hakkında bilgilendirme
    '''
    print(f'x: {x}')
class Person:
    def speak(self):
        print('I am speaking...')

# 2_math_modulu.py
# Yöntem 1
# import math
# import math as islem
# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)
# value = islem.factorial(5)
# Yöntem 2
# from math import *
def sqrt(x):
    print('x :'+ str(x))
from math import factorial,sqrt,ceil
# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)
print(value)

# 3_random_modulu.py
import random
# result = dir(random)
# result = help(random)
result = random.random() # 0.0 - 1.0
result = random.random() * 100
result = int(random.uniform(10,100))
result = random.randint(1,100)
greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
# result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)
liste = list(range(10))
random.shuffle(liste)
result = liste
liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 2)
print(result)
