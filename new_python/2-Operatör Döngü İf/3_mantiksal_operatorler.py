# =====================================================
# Mantıksal Operatörler (and, or, not)
# =====================================================

x = 5
hak = 0
devam = 'e'
print((x > 5) and (x < 10))
print((hak > 0) and (devam == 'e'))
print((x > 0) or (x % 2 == 0))
print(not(x > 0))
print(((x>5) and (x<10)) and (x%2==0))

# Pozitif çift sayı kontrolü
# sayi = int(input('sayı: '))
# result = (sayi > 0) and (sayi % 2 ==0)
# print(f'girilen sayı pozitif çift sayı mı: {result}')

# Email ve parola ile giriş kontrolü
# email = 'email@sadikturan.com'
# password = 'abc123'
# girilenEmail = input('email: ')
# girilenPassword = input('password: ')
# result = (girilenEmail == email) and (girilenPassword == password)
# print(f'uygulamaya giriş başarılı mı: {result}')

# 3 sayıdan en büyüğü
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# result = (a > b) and  (a > c)
# print(f'a en büyük sayıdır : {result}')
# result = (b > a) and (b > c)
# print(f'b en büyük sayıdır : {result}')
# result = (c > a) and (c > b)
# print(f'c en büyük sayıdır : {result}')
