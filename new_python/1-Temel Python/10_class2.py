class Question:
    def __init__(self, text, choices, answer):
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
            print(f"Puanınız: %{round((self.score * 100) / len(self.questions), 1)}")
        else:
            self.displayQuestion()

q1 = Question("En iyi programlama dili hangisidir?", ["Python", "Java", "C#"], "Python")
q2 = Question("En popüler renk?", ["Kırmızı", "Mavi", "Yeşil"], "Mavi")
q3 = Question("2 + 2 kaçtır?", ["3", "4", "5"], "4")
questions = [q1, q2, q3]
quiz = Quiz(questions)
quiz.displayQuestion()
print("\n" + 20 * '-' + "\n")

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
            else:
                bakiyeSorgula(hesap)
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limiti: {hesap['ekHesap']} TL")
    
KerimHesap = {
    'ad': 'Kerim Yılmaz',
    'hesapNo': '98765432',
    'bakiye': 3000,
    'ekHesap': 2000
}
AsımHesap = {
    'ad': 'Asım Turan',
    'hesapNo': '46345602',
    'bakiye': 2000,
    'ekHesap': 1000
}
paraCek(KerimHesap, 3500)
paraCek(KerimHesap, 2000)
paraCek(AsımHesap, 3000)

class BankaHesap:
    def __init__(self, ad, hesapNo, bakiye, ekHesap):
        self.ad = ad
        self.hesapNo = hesapNo
        self.bakiye = bakiye
        self.ekHesap = ekHesap

    def para_cek(self, miktar):
        print(f"Merhaba {self.ad}")
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print('Paranızı alabilirsiniz.')
            self.bakiye_sorgula()
        else:
            toplam = self.bakiye + self.ekHesap
            if toplam >= miktar:
                ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h): ')
                if ekHesapKullanimi == 'e':
                    ekhesapKullanilacakMiktar = miktar - self.bakiye
                    self.bakiye = 0
                    self.ekHesap -= ekhesapKullanilacakMiktar
                    print('Paranızı alabilirsiniz.')
                    self.bakiye_sorgula()
                else:
                    print(f"{self.hesapNo} nolu hesabınızda {self.bakiye} TL bulunmaktadır.")
            else:
                print('Üzgünüz, bakiye yetersiz.')
                self.bakiye_sorgula()

    def bakiye_sorgula(self):
        print(f"{self.hesapNo} nolu hesabınızda {self.bakiye} TL bulunmaktadır. Ek hesap limiti: {self.ekHesap} TL")

sadik_hesap = BankaHesap('Sadık Turan', '13245678', 3000, 2000)
ali_hesap = BankaHesap('Ali Turan', '12345678', 2000, 1000)

sadik_hesap.para_cek(3500)
sadik_hesap.para_cek(2000)
ali_hesap.para_cek(3000)
