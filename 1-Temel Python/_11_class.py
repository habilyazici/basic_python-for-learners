class Person:
    address = 'no information'
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

p1 = Person(name='ali', year= 1990) 
p2 = Person("yağmur", 1995)
p1.name = 'ahmet'
Person.address = 'izmir'
p1.address = 'kocaeli' 
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')
print(p2)
print(type(p1))
print(p1 == p2)
print("\n" + 20 * '-' + "\n")

class Movie():
    movieCount = 0
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        Movie.movieCount += 1
        print('movie objesi oluşturuldu.')

    # dunder methotlar python methotlarını ezer veya beraber kullanır
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        # program sonlandığında çalışır.
        print(f'{self.title} film objesi silindi.')

m = Movie('film adı','yönetmen adı',120)
print(str(m))
print(len(m))
print("\n" + 20 * '-' + "\n")

class PersonBase():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print(f'I am a person. My name is {self.firstName} {self.lastName}.')
    def eat(self):
        print('I am eating' )

    # static method class method'udur yani classtaki instancelerden bağımsızdır. İlla init ile nesne oluşturulması gerekmiyor.
    @staticmethod
    def sayHello():
        return print('Hello I am a person')
    
class Student(PersonBase):
    def __init__(self, fname, lname, number):
        super().__init__(fname, lname)
        self.studentNumber = number
        print('Student Created')

    def who_am_i(self):
        print(f'I am a student. My name is {self.firstName} {self.lastName}. My student number is {self.studentNumber}.')
    # parentte de sayhHello metodu var o yüzden override oldu.
    def sayHello(self):
        print('Hello I am a student')

class Teacher(PersonBase):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a teacher. My name is {self.firstName} {self.lastName}. My branch is {self.branch}.')

person1 = PersonBase("Ali", "Veli")
student1 = Student("Ayşe", "Yılmaz", 123)
teacher1 = Teacher("Mehmet", "Demir", "Math")

print(student1.studentNumber)
teacher1.who_am_i()
person1.who_am_i()
student1.eat()
PersonBase.sayHello()
teacher1.sayHello()
student1.sayHello()
# print("\n" + 20 * '-' + "\n")