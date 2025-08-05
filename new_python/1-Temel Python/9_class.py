# Sınıflar, OOP ve Uygulama Örnekleri

# Temel class örneği
class Person:
    address = 'no information'
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
# object (instance)
p1 = Person(name='ali', year= 1990) 
p2 = Person(name ='yağmur', year = 1995)
p1.name = 'ahmet'
p1.address = 'kocaeli' 
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

# Gelişmiş class örneği
class Circle:
    pi = 3.14
    def __init__(self, yaricap=1):
        self.yaricap = yaricap
    # Methods

# Special methods
class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print('film objesi silindi')
m = Movie('film adı','yönetmen adı',120)
print(str(m))

# Inheritance (Kalıtım)
class PersonBase():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')
    def who_am_i(self):
        print('I am a person')
    def eat(self):
        print('I am eating')
class Student(PersonBase):
    def __init__(self, fname, lname, number):
        PersonBase.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')
    def who_am_i(self):
        print('I am a student')
    def sayHello(self):
        print('Hello I am a student')
class Teacher(PersonBase):
    def __init__(self,fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

# Soru ve Quiz uygulaması
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')
        for q in question.choices:
            print('-'+ q)
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()
    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            print('Quiz bitti')
        else:
            self.displayQuestion()

# Bankamatik uygulaması
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')
            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadir.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)
SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}
AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}
# Bakiye sorgulama fonksiyonu eksikti, ekleniyor
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limiti: {hesap['ekHesap']} TL")
# Hesap makinesi uygulaması
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi== "toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(3,4))
    elif islem_adi == "bolme":
        print(f4(10,2))
    else:
        print("geçersiz işlem...")
islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "carpmaa")
