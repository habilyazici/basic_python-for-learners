x='En dıştaki değişken'
def func1():
    x= "clas1'deki değişken"
    print(x)
func1()
print(x)
print("\n" + 20 * '-' + "\n")

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

# LEGB - Program, değişkeni hafızaya alıp çalıştırırken ilk bu sırada bakar ilk olarak local değişken mi değilmi sonrasında enclosing değişken mi, sonrasında global değişken mi, sonrasında ise built in func değişkeni mi

print("\n" + 20 * '-' + "\n")
global_var = 'Ben globalim!'

def yerel_kullan():
    local_var = 'Ben yerelim!'
    print('Fonksiyon içinden yerel:', local_var)
yerel_kullan()
print("\n" + 20 * '-' + "\n")

x = 'ilk global'
def global_degistir():
    global x
    x = 'fonksiyonda değişti'
    print('Fonksiyon içinden x:', x)
global_degistir()
print('Fonksiyon dışından x:', x)
print("\n" + 20 * '-' + "\n")

# scope örneği: fonksiyon içindeki yerel değişken dışarıdan erişilemez
def scope_ornek():
    global y
    y = 'global fonksiyon içinde'
    print('Fonksiyon içinden y:', y)
scope_ornek()
print('Fonksiyon dışından y:', y)
print("\n" + 20 * '-' + "\n")