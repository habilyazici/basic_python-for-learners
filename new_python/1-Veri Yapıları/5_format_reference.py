
# =====================================================
# 1. Format ve Referans Kavramı
# =====================================================

# --- format.py ---
name = 'Çınar'
surname = 'Turan'
age = 36
# print('My name is {} {}'.format(name, surname))
# print('My name is {1} {0}'.format(name, surname))
# print('My name is {s} {n}'.format(n=name, s=surname))
# print("My name is {} {} and I'm {} years old.".format(name, surname, age))
# print("My name is {} {} and I'm {} years old.".format(name, name, name))
# result = 200 / 700
# print('the result is {r:1.4}'.format(r=result))
print(f"My name is {name} {surname} and I'm {age} years old.")
print()

# --- reference.py ---
# value types => string, number

x = 5
y = 25
x = y
y = 10
# print(x,y)
# reference types => list
a = ["apple","banana"]
b = ["apple","banana"]
a = b
b[0] = "grape"
print(a, b)
print()
