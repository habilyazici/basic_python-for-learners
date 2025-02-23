#TUPLE
# Liste elemanlarında yapılabilen bir çok şeyi tuple'da yapamıyorsun örnek: append, del vs...
# Değişken tek cümle yapısına bağlıysa string, birden fazla cümle yapısına bağlıysa tuple olmaktadır.
# ister parantez ister tırnak kullan ikiside tuple'dır.
capitals= ('ankara',' izmir ', 'rize','kayseri') # or   şehir= ('ankara',)   tuplem= 22, 23423, 'habil'
capitals=('berlin','paris')
print(type(capitals))
print(len(capitals))
print(capitals[0])
print(tuple('demet'))
# tupplelar diğer veri yapılarına göre çok hızlıdır ve daha az yer kaplar. Ayrıca değiştirilemediği için de güvenilirdir.

# Set yapıları sırasız ve listelerin aksina tek yapılardır yani sette oluşturulan verilerin bir sırası yoktur. Aynı veriler tek gözükür.
sehirler= {'mardin', ' bitlis', 'adıyaman', ' bitlis'}
sehirler.add('gaziantep')
sehirler.update(['artvin', 'batum'])
sehirler.remove('mardin')
sehirler.discard('adıyaman')
print(sehirler)
# remove ile sette olmayan bir elemanı silersen hata alırsın ama discardda hata mata yok.
sehirler.clear() # del cities' de kullanılabilir ama clear boş bir set yapısını çıktı verirken del direkt siliyor.

yeni_tuple= (22, 22 ,32 , [223, 342], 34)
yeni_tuple[3][0]= 17
# Tuple da veri değiştirme yok yedik ama tupple içerisindeki bir listede değişme yapılabilmektedir.
print(32 in yeni_tuple)
print(yeni_tuple)

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