import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - numbers2
result = numbers1 - 10
result = numbers1 * numbers2
result = numbers1 * 10
result = numbers1 / numbers2
result = numbers1 / 10

result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

# print(mnumbers1)
# print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2))
result = np.hstack((mnumbers1,mnumbers2))

result = numbers1 >= 50
result = numbers1 % 2 == 0

print(numbers1[result])

print(result)

np_array = np.random.randint(-20, 20, 20)
np_multi = np_array.reshape(5, 4)
np_multi = np_multi * 3
print('np_multi:\n', np_multi)
ciftler = np_multi[np_multi % 2 == 0]
print('ciftler: ', ciftler)
print('ciftler > 0: ', ciftler[ciftler > 0])
print("\n" + 20 * '-')