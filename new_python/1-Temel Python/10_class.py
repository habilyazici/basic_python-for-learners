class Person:
    address = 'no information'
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

p1 = Person(name='ali', year= 1990) 
p2 = Person("yağmur", 1995)
p1.name = 'ahmet'
p1.address = 'kocaeli' 
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')
print(p2)
print(type(p1))
print(p1 == p2)
print("\n" + 20 * '-' + "\n")

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
        print(f'{self.title} film objesi silindi.')

m = Movie('film adı','yönetmen adı',120)
print(str(m))
print("\n" + 20 * '-' + "\n")

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
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = PersonBase("Ali", "Veli")
s1 = Student("Ayşe", "Yılmaz", 123)
t1 = Teacher("Mehmet", "Demir", "Math")

p1.who_am_i()
s1.who_am_i()
s1.sayHello()
t1.who_am_i()
print("\n" + 20 * '-' + "\n")
