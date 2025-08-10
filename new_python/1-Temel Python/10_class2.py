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
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limiti: {hesap['ekHesap']} TL")
    
paraCek(SadikHesap, 3500)
paraCek(SadikHesap, 2000)
paraCek(AliHesap, 3000)
