#TUPLE
# Liste elemanlarında yapılabilen bir çok şeyi tuple'da yapamıyorsun örnek: append, del vs...
# Değişken tek cümle yapısına bağlıysa string, birden fazla cümle yapısına bağlıysa tuple olmaktadır.
# ister parantez ister tırnak kullan ikiside tuple'dır.
list2 = ['ali','veli']
tuple2 = ('damla','ayşe','ayşe')
names1 = ('demet','emel','ayşe') + tuple2
print(names1)
list2[0] = 'ahmet'
# tuple2[0] = 'deniz'  # Hata verir
print(tuple2.count('ayşe'))
print(tuple2.index('ayşe'))
print("\n" + 20 * '-' + "\n")

# Set yapıları sırasız ve listelerin aksina tek yapılardır yani sette oluşturulan verilerin bir sırası yoktur. Aynı veriler tek gözükür.
fruits1 = { 'orange', 'apple', 'banana'}
# print(fruits1[0]) indekslenemez

for x in fruits1:
    print(x)
fruits1.add('cherry')
fruits1.update(['mango','grape','apple'])
fruits1.remove('mango')
# remove ile sette olmayan bir elemanı silersen hata alırsın ama discardda hata mata yok.
fruits1.discard('apple')
print(fruits1)
fruits1.pop()
fruits1.clear()
print(fruits1)

myList1 = [1,2,5,4,4,2,1]
print(set(myList1))
print()

yeni_tuple2= ('izmir', 'ankara', 'izmir', 'nevşehir')
yeni_set= set(yeni_tuple2)
print(yeni_set)

yeni_tuple4= ('mehmet', 'hüseyin', 'mehmet', 'ali')
yeni_tuple5 = tuple(set(yeni_tuple4))
print(yeni_tuple5)

new_string= 'alskdjglkasdjgklasdgkjawoıjdkşxb'
new_set= set()
for harf in new_string:
    new_set.add(harf)
print(new_set)