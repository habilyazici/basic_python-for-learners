import numpy as np

py_array = [1,2,3,4,5,6,7,8,9]
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_array))
print(type(np_array))
print("\n" + 20 * '-')

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)
# tek boyutlu dizi, 3x3 tablo boyutuna uygun iki boyutlu bir diziye yani 3x3 lük bir matrise dönüşüyor.
print(py_multi)
print(type(py_multi))
print(np_multi)
print(type(np_multi))
print("\n" + 20 * '-')

print("Dizi boyutu:", np_array.ndim)
print("Matris boyutu:", np_multi.ndim)

print("Dizi şekli:", np_array.shape)
print("Matris şekli:", np_multi.shape)
print("\n" + 20 * '-')

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
print("\n" + 20 * '-')

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