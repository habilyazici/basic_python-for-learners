import numpy as np

print("aralık: ", np.arange(1,10))
print("aralık 3er artarak: ", np.arange(10,100,3))
print("aralık rastgele 3 sayı: ", np.random.choice(np.arange(10, 101), size=3, replace=False))
# sayı. şeklinde olanlar float anlamına geliyor
print("sıfırlar: ", np.zeros(10))
print("birler: ", np.ones(10))
print("\n" + 20 * '-' + "\n")

print("eşit aralık: ",   np.linspace(0,5,5))
print("rastgele 0 - 10 tam sayılar: ", np.random.randint(0,10))
print("rastgele 0 - 23 tam sayılar: ", np.random.randint(23))
print("rastgele -10 - 10 tam sayılar: ", np.random.randint(-10,10,3))
print("rastgele 0 - 20 reel sayılar: ", np.random.uniform(0,20,5))
print("rastgele + reel sayılar: ", np.random.rand(5))
print("rastgele -,+ reel sayılar: ", np.random.randn(5))
print("\n" + 20 * '-' + "\n")

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi)
print("sutun toplamı: ", np_multi.sum(axis=0))
print("satır toplamı: ", np_multi.sum(axis=1))
print("\n" + 20 * '-' + "\n")

rnd_numbers = np.random.randint(-10,100,10)
print("rastgele sayılar: ", rnd_numbers)
print("maksimum değer: ", rnd_numbers.max())
# min(), mean(), std(), argmin(), argmax(), var()
print("\n" + 20 * '-' + "\n")

# indexleme indexing
numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])
print('numbers 0. index ', numbers[0])
print('numbers 3. index ', numbers[2])
print('numbers son eleman ', numbers[-1])
print("\n" + 20 * '-' + "\n")

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print("numbers2 3*3 matrisi:\n", numbers2)
print('numbers2[0] satırı: ', numbers2[0])
print('numbers2[2] satırı: ', numbers2[2])
print("\n" + 20 * '-' + "\n")

# dilimleme slicing
print('tüm satırlar:\n', numbers2[0:3])
print('ilk 3 satır:\n', numbers2[:3])
print('ilk 2 satır:\n', numbers2[:2])
print('2. satırdan sonrasını:\n', numbers2[2:])
print('tüm satırlar:\n', numbers2[:])
print('tüm satırlar:\n', numbers2[::])
print('ters sırayla tüm satırlar:\n', numbers2[::-1])
print("\n" + 20 * '-' + "\n")

# iki boyutlu bir matriste indexleme yaparken ilk kısım satır ve ikinci kısım sütundur
print('numbers2 1. satır 3. sütun: ', numbers2[0,2])
print('numbers2 2. satır 2. sütun: ', numbers2[1,1])
print('numbers2 2. ve 3. satır 1. sütun: ', numbers2[1:3,0])
print('numbers2 tüm satırlar 3. sütun: ', numbers2[:,2])
print('numbers2 tüm satırlar 1 ve 2. sütunlar:\n', numbers2[:,0:2])
print('numbers2 son satır tüm sütunlar: ', numbers2[-1,:])
print('numbers2 ilk 2 satır son 2 sütun:\n', numbers2[:2,1:])
print("\n" + 20 * '-' + "\n")

arr1 = np.arange(0,10)
arr2 = arr1.copy()
arr2[0] = 20
print(arr1)
print(arr2)
print("\n" + 20 * '-' + "\n")