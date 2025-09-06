from dbmanager import DbManager
from Student import Student
from Teacher import Teacher

import datetime
print("\n" + 20 * '-' + "\n")

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "\n*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmenleri göster\n6-Öğretmen Ekle\n7-Öğretmen Güncelle\n8-Derslerin bilgilerini göster\n9-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
            elif islem == '5':
                self.displayTeachers()
            elif islem == '6':
                self.addTeacher()
            elif islem == '7':
                self.editTeacher()
            elif islem == '8':
                self.LessonsInfo()
            elif islem == '9' or islem == 'E' or islem == 'Ç':
                break
            else:
                print('yanlış seçim')

    def displayStudents(self):
        self.displayClasses()

        classid = int(input('Sınıfın ID\'si: '))
        students = self.db.getStudentsByClassId(classid)
        print("\nÖğrenci Listesi")
        for std in students:
            print(f' öğrencinin id: {std.id}, öğrencinin adı: {std.name}, öğrencinin soyadı: {std.surname}, doğum tarihi: {std.birthdate}, cinsiyeti: {std.gender}, sınıfı: {std.classid}')

    def addStudent(self):
        self.displayClasses()

        classid = int(input('Sınıfın ID\'si: '))
        number = input('Numara: ')
        name = input('Ad: ')
        surname = input('Soyad: ')
        year = int(input('Yıl: '))
        month = int(input('Ay: '))
        day = int(input('Gün: '))
        birthdate = datetime.date(year, month, day)
        # birthdate = f"{year}-{month}-{day}"
        gender = input('Cinsiyet (E/K): ')

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addorEditStudent(student)

    def editStudent(self):
        self.displayStudents()
        studentid = int(input('öğrenci id: '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('name:') or student[0].name
        student[0].surname = input('surname:') or student[0].surname
        student[0].gender = input('cinsiyet (E/K):') or student[0].gender
        student[0].classid = input('sınıf: ') or student[0].classid

        year = input("yıl: ") or student[0].birthdate.year
        month = input("ay: ") or student[0].birthdate.month
        day = input("gün: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.addorEditStudent(student[0]) 

    def deleteStudent(self):
        self.displayStudents()
        studentid = int(input('öğrenci id: '))

        self.db.deleteStudent(studentid)

    def displayClasses(self):
        print("\nSınıflar:")
        classes = self.db.getClasses()
        for clas in classes:
            print(f'{clas.id}: {clas.name}')

    def displayTeachers(self):
        teachers = self.db.getTeachers()
        print("Öğretmen Listesi")
        for t in teachers:
            print(f'{t.id}: Öğretmen: {t.name} {t.surname} | Doğum Tarihi: {t.birthdate} | Cinsiyet: {t.gender} | Branşı: {t.branch}')

    def addTeacher(self):
        self.displayTeachers()

        branch = input('Branş: ')
        name = input('Ad: ')
        surname = input('Soyad: ')
        year = int(input('Yıl: '))
        month = int(input('Ay: '))
        day = int(input('Gün: '))
        birthdate = datetime.date(year, month, day)
        gender = input('Cinsiyet (E/K): ')
        teacher = Teacher(None, branch, name, surname, birthdate, gender)
        self.db.addorEditTeacher(teacher)

    def editTeacher(self):
        self.displayTeachers()

        teacher_id = int(input('Düzenlenecek öğretmen id: '))
        teacher_obj = self.db.getTeacherById(teacher_id)[0]

        branch = input('Yeni branş: ') or teacher_obj.branch
        name = input('Yeni ad: ') or teacher_obj.name
        surname = input('Yeni soyad: ') or teacher_obj.surname
        year = input('Yeni yıl: ') or teacher_obj.birthdate.year
        month = input('Yeni ay: ') or teacher_obj.birthdate.month
        day = input('Yeni gün: ') or teacher_obj.birthdate.day
        birthdate = datetime.date(int(year), int(month), int(day))
        gender = input('Yeni cinsiyet (E/K): ') or teacher_obj.gender
        teacher = Teacher(teacher_id, branch, name, surname, birthdate, gender)
        self.db.addorEditTeacher(teacher)

    def LessonsInfo(self):
        lessons_details = self.db.getLessons()
        print("id ye göre Ders Listesi")
        for lesson_details in lessons_details:
            print(f"{lesson_details[0]} dersinin sınıf adı: {lesson_details[1]} ve öğretmen adı: {lesson_details[2]} {lesson_details[3]}")

app = App()     
app.initApp()