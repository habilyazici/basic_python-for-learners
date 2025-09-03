class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    SumQuizCount = 0
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        Quiz.SumQuizCount += 1
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
        if self.getQuestion().checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            print('Quiz bitti')
            print(f"Puanınız: %{round((self.score * 100) / len(self.questions), 1)}")
        else:
            self.displayQuestion()

question1 = Question("En iyi programlama dili hangisidir?", ["Python", "Java", "C#"], "Python")
question2 = Question("En popüler renk?", ["Kırmızı", "Mavi", "Yeşil"], "Mavi")
question3 = Question("2 + 2 kaçtır?", ["3", "4", "5"], "4")
questions = [question1, question2, question3]
quiz = Quiz(questions)
quiz.displayQuestion()
print("\n" + 20 * '-' + "\n")

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

json_veri = [
    {
        'ad': 'Sadık Turan',
        'hesapNo': '13245678',
        'bakiye': 3000,
        'ekHesap': 2000
    },
    {
        'ad': 'Ali Turan',
        'hesapNo': '12345678',
        'bakiye': 2000,
        'ekHesap': 1000
    },
    {
        'ad': 'Ayşe Yılmaz',
        'hesapNo': '87654321',
        'bakiye': 5000,
        'ekHesap': 1500
    }
]

users = []
for user in json_veri:
    users.append(BankaHesap(**user))
print(users)

# Her hesap için para çekme işlemi
cekilecek_miktarlar = [3500, 2000, 3000]
for user, miktar in zip(users, cekilecek_miktarlar):
    user.para_cek(miktar)