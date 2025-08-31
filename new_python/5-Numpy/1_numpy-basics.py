import numpy as np

py_array = [1,2,3,4,5,6,7,8,9]
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(py_array[2])
print(np_array[2])
print(type(py_array))
print(type(np_array))
print("\n" + 20 * '-' + "\n")

# tek boyutlu dizi, iki boyutlu bir diziye yani 3x3 lük bir matrise dönüşüyor.
py_array2 = [1,2,3,4,5,6,7,8,9] 
py_array2 = [[1,2,3], [4,5,6], [7,8,9]]
np_array2 = np.array(py_array2)
np_multi2 = np_array2.reshape(3,3)
print(np_multi2)
print("\n" + 20 * '-' + "\n")

result1 = np.array([1,2,3,4,5,6,7,8,9])
result2 = result1.reshape(3,3)
result3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(result1)
print(result2)
print(result3)
print(type(result1))
print(type(result2))
print(type(result3))
print("\n" + 20 * '-' + "\n")

print("Dizi boyutu:", result1.ndim)
print("Matris boyutu:", result2.ndim)
print("Matris boyutu:", result3.ndim)

print("Dizi şekli:", result1.shape)
print("Matris şekli:", result2.shape)
print("Matris şekli:", result3.shape)
print("\n" + 20 * '-' + "\n")

matris_3d = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print(matris_3d)
print("Boyut sayısı:", matris_3d.ndim)
print("Şekli:", matris_3d.shape)
print("\n" + 20 * '-' + "\n")

matris_4d = np.array([
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24]
        ]
    ],
    [
        [
            [25, 26, 27, 28],
            [29, 30, 31, 32],
            [33, 34, 35, 36]
        ],
        [
            [37, 38, 39, 40],
            [41, 42, 43, 44],
            [45, 46, 47, 48]
        ]
    ]
])

print(matris_4d)
print("Boyut sayısı:", matris_4d.ndim)
print("Şekli:", matris_4d.shape)