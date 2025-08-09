# True 1 False 0 demek demektir
x= 2
y= 1
print(x>1)
print(type(x>1))

z=     x >= y and x!= y
print(z)

list1= ['ahmet', 'mehmet']
list2= ['ahmet', 'mehmet']
print(list1==list2)
print(list1 is list2)
# Buradaki iki eşit işareti direkt olarak değerin aynı olup olmadığına bakar, is ise aynı nesneye ait olup olmadığını söyler

h= 1
j= True
print(h==1)
print(h is j)

print(True and True) # print(4<38 and 8<45)
print(True or False)
print(not False)