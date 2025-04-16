x='En dıştaki değişken'
def func1():
    x= "clas1'deki değişken"
    print(x)
func1()
print(x)

y='En dıştaki değişken'
def funca():
    y= "clas1'deki değişken"
    def funcb():
        y= "clas2'deki değişken"
        print(y)
    funcb()
funca()


z='En dıştaki değişken'
def fonk1():
    z= "clas1'deki değişken"
    def fonk2():
        print(z)
    fonk2()
fonk1()

# LEGB - Program değişkeni hafızaya alıp çalıştırırken ilk bu sırada bakar ilk olarak local değişken mi değilmi
# sonrasında enclousing değişken mi, sonrasında global değişken mi, sonrasında ise built in func değişkeni mi
# Global veya scope ile iki değişkeni yerel veya global erişir hale getirebilirsin.