import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
print(numbers1)
print(numbers2)
print("\n" + 20 * '-' + "\n")

print("iki array toplamı ", numbers1 + numbers2)
print("arraye ekleme ", numbers1 + 10)
print("iki array çıkarma ", numbers1 - numbers2)
print("array çıkartma ", numbers1 - 10)
print("array çarpma ", numbers1 * numbers2)
print("array çarpma ", numbers1 * 10)
print("array bölü ", numbers1 / numbers2)
print("array bölü ", numbers1 / 10)
print("\n" + 20 * '-' + "\n")

print("sin array ", np.sin(numbers1))
print("cos array ", np.cos(numbers1))
print("sqrt array ", np.sqrt(numbers1))
print("log array ", np.log(numbers1))
print("\n" + 20 * '-' + "\n")

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
result1 = np.vstack((mnumbers1, mnumbers2))
result2 = np.hstack((mnumbers1, mnumbers2))
print('vstack sonucu:', result1)
print('hstack sonucu:', result2)
print('vstack ndim:', result1.ndim)
print('hstack ndim:', result2.ndim)
print('vstack shape:', result1.shape)
print('hstack shape:', result2.shape)
print("\n" + 20 * '-' + "\n")

print("numbers1 >= 50:  ", numbers1[numbers1 >= 50])
print("numbers1 % 2 == 0:  ", numbers1[numbers1 % 2 == 0])
print("\n" + 20 * '-' + "\n")

np_array = np.random.randint(-20, 20, 20)
np_multi = np_array.reshape(5, 4)
np_multi = np_multi * 3
print('np_multi:\n', np_multi)
ciftler = np_multi[np_multi % 2 == 0]
print('ciftler: ', ciftler)
print('ciftler > 0: ', ciftler[ciftler > 0])
print("\n" + 20 * '-')