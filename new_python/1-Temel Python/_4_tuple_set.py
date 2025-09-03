#TUPLE
# Liste elemanlarında yapılabilen bir çok şeyi tuple'da yapamıyorsun örnek: append, del vs...
# Değişken tek cümle ise string, birden fazla virgül varsa tuple olmaktadır.
# ister parantez ister tırnak kullan ikiside tuple'dır.
list2 = ['ali','veli']
tuple2 = ('damla','ayşe','ayşe')
names1 = ('demet','emel','ayşe') + tuple2
print(names1)
list2[0] = 'ahmet'
# tuple2[0] = 'deniz'  # Hata verir
print(names1.count('ayşe'))
print(names1.index('ayşe'))
print("\n" + 20 * '-' + "\n")

# Set yapıları sırasız ve listelerin aksina tek yapılardır yani sette oluşturulan verilerin bir sırası yoktur.
fruits1 = { 'orange', 'apple', 'banana'}
# print(fruits1[0]) indekslenemez

for x in fruits1:
    print(x)
fruits1.add('cherry')
fruits1.update(['mango','grape','apple'])
fruits1.remove('mango')
fruits1.discard('apple')
# remove ile sette olmayan bir elemanı silersen hata alırsın ama discardda hata mata yok.
print(fruits1)
fruits1.pop()
fruits1.clear()
print(fruits1)
print("\n" + 20 * '-' + "\n")

myList1 = [1,2,5,4,4,2,1]
print('set edilmiş hali: ', set(myList1))

yeni_tuple4= ('mehmet', 'hüseyin', 'mehmet', 'ali')
yeni_tuple5 = tuple(set(yeni_tuple4))
print('tuple edilmiş hali:', yeni_tuple5)

new_string= 'alskdjglkasdjgklasdgkjawoıjdkşxb'
new_set= set()
for harf in new_string:
    new_set.add(harf)
print('set edilmiş hali: ', new_set)