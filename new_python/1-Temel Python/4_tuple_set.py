list2 = ['ali','veli']
tuple2 = ('damla','ayşe','ayşe')
names1 = ('demet','emel','ayşe') + tuple2
print(names1)
list2[0] = 'ahmet'
# tuple2[0] = 'deniz'  # Hata verir
print(tuple2.count('ayşe'))
print(tuple2.index('ayşe'))
print("\n" + 20 * '-' + "\n")

fruits1 = { 'orange', 'apple', 'banana'}
# print(fruits1[0]) indekslenemez

for x in fruits1:
    print(x)
fruits1.add('cherry')
fruits1.update(['mango','grape','apple'])
fruits1.remove('mango')
fruits1.discard('apple')
print(fruits1)
fruits1.pop()
fruits1.clear()
print(fruits1)

myList1 = [1,2,5,4,4,2,1]
print(set(myList1))
print()
