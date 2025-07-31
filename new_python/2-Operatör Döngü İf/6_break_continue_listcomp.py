# =====================================================
# break, continue, range, enumerate, zip, list comprehensions
# =====================================================

# break-continue örnekleri
# name = 'Sadık Turan'
# for letter in name:
#     if letter == 'ı':
#         continue
#     print(letter)
# x = 0
# while x < 5:    
#     x+=1
#     if x == 2:
#         continue
#     print(x)
# 1- 100 e kadar tek sayıların toplamı
x = 0
result = 0
while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x
print(f'toplam: {result}')

# range, enumerate, zip örnekleri
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(list(zip(list1, list2, list3)))
for item in zip(list1, list2, list3):
    print(item)
for a,b,c in zip(list1, list2, list3):
    print(a,b,c)

# list comprehensions
numbers = [x for x in range(10)]
print(numbers)
numbers = [x**2 for x in range(10)]    
print(numbers)
numbers = [x*x for x in range(10) if x%3==0]
print(numbers)
