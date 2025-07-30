class car:
    def __init__(self, brand, model, year, color):
        # initialize yapmak nesneyi oluşturmak
        # self ise nesneyle paramtreleri eşleştirmek
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        # instance proporties
    def car_brand(self):
        return f"arabanın markası '{self.brand}' ve arabanın üretim yılı '{self.year}''dır"
        # instance method

# instance
car1 = car('bmw', 'M-series', 2025, 'black')
car2 = car('audi', 'A8', 2020, 'Green')
car3 = car('toyota', 'corolla', 2017, 'White')

print(car1.year)
print(car1.car_brand())

class student:
    school_name='Dokuz Eylül'
    def __init__(self, name, surname, major):
        self.name=name
        self.surname=surname
        self.major=major

    def school_name_method(self, new_school):
        self.school_name = new_school
        return f"okulun adı {self.school_name}"

student1= student('ahmet', 'korkmaz', 'Computer Science')
student2= student('aslı', 'gür', 'physics')

student1.name= 'ismail'
print(student1.name)
print(student1.school_name)
print(student2.school_name_method("Ege Üniversitesi"))

class movies:
    watched_movies = 0
    def __init__(self, name, director, release_year, rating, time):
        self.name = name
        self.director = director
        self.release_year = release_year
        self.rating = rating
        self.time = time
        movies.watched_movies +=1
        # initialize zaten yeni nesne yaratılınca çalışan bir method dolayısıyla o sırada bu kodda "çalışır"

    def what_time(self):
        hours = self.time//60
        minutes = self.time%60
        return f"film {hours} saat {minutes} dakika"

print( f"şuanda izlenen film sayısı {movies.watched_movies}")

film1 = movies("The Shawshank Redemption", "Frank Darabont", 1994, 9.3, 142)
film2 = movies("The Godfather", "Francis Ford Coppola", 1972, 9.2, 175)

print( f"şuanda izlenen film sayısı {movies.watched_movies}")
print(film2.what_time())


class Person:
    population = 0
    country = "Turkey"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Person.population += 1
    # classmethodlar class'ın özelliklerini değiştirebilen methodlardır
    @classmethod
    def population_change(cls, new_population):
        cls.population = new_population
        return cls.population
    @classmethod
    def country_change(cls, new_country):
        cls.country = new_country
        return cls.country
    @staticmethod
    def static():
        return "bu mesaj bilgilendimre amaçlıdır"
    # class yapsısına ait ama özelliklerden bağımsız bir method'tur

person1 = Person("Ali", "korkmaz")
person2 = Person("Ayşe", "Sevin")

print("Population:", Person.population)
print("New total population", person2.population_change(23))
print(Person.population)
print("New country", person1.country_change("ABD"))
print(Person.country)
print(Person.static())


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        return "Bu hayvan ses çıkartan bir hayvandır"
    def info(self):
        return f"Bu {self.name} {self.age} yaşındadır"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def speak(self):
        return "Hav! Hav!"
    def info(self):
        base_info = super().info()
        return f"{base_info} ve cinsi {self.breed}'dir"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        new_speak = super().speak()
        return f"{new_speak} ve bu ses miyav miyav'dır"
    def info(self):
        base_info = super().info()
        return f"{base_info} Bu kedinin rengi {self.color}'dir"

dog1 = Dog("Buddy", 3, "Golden Retriever")
cat1 = Cat("Whiskers", 2, "gri")

print(dog1.speak())
print(dog1.info())
print(cat1.speak())
print(cat1.info())
# print(help(Cat))

# dunder metotları önceden tanımlı metotlardır, başında ve sonunda çift alt çizgi vardır.
numbers = int.__add__(4,87)
print(numbers)

class num_length:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    def __mydunder__(self):
        count = 0 
        for hane in str(self.number):
            count += 1
        return count
# print(dir(num_length))
new_number = num_length(1925235, "birinci sayı")
print(f"bu girilen {new_number.name} kaç haneden oluştuğu: {new_number.__mydunder__()} ...")

class Kisi:
    def __init__(self, isim):
        self.__isim = isim
# __ gerçek özel değişken yapar ve kisi1.__isim şeklinde veriye erişilemez. Yani veri güvenliği sağlar.

    @property
# property ise bir methodu, class özellik(proporties) yapar bu sayede parantezler kullanmaya gerek kalmaz
    def Name(self):
        return self.__isim

    def Name2(self, yeni_isim):
        if not isinstance(yeni_isim, str):
            raise ValueError("İsim bir metin olmalıdır.")
        self.__isim = yeni_isim
        return self.__isim

kisi1 = Kisi("Ahmet")
print(kisi1.Name)

kisi1.Name2 = "Mehmet"
print(kisi1.Name2)