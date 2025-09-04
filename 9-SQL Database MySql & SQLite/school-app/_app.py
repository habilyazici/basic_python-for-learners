from _dbmanager import DbManager
from _Student import Student
from _Teacher import Teacher

import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Öğretmen Güncelle\n7-Dersleri göster\n8-Çıkış(E/Ç)"
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
                self.addTeacher()
            elif islem == '6':
                self.editTeacher()
            elif islem == '7':
                self.displayLessons()
            elif islem == '8' or islem == 'E' or islem == 'Ç':
                break
            else:
                print('yanlış seçim')

    def displayStudents(self):       
        self.db.getClasses()
        classid = int(input('Sınıfın ID\'si: '))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

    def addStudent(self):
        self.db.getClasses()
        classid = int(input('Sınıfın ID\'si: '))
        number = input('Numara: ')
        name = input('Ad: ')
        surname = input('Soyad: ')
        year = int(input('Yıl: '))
        month = int(input('Ay: '))
        day = int(input('Gün: '))
        birthdate = datetime.date(year, month, day)
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
        self.db.editStudent(student[0]) 

    def deleteStudent(self):
        self.displayStudents()
        studentid = int(input('öğrenci id: '))

        self.db.deleteStudent(studentid)

    def displayClasses(self):
        classes = self.db.getClasses()
        for clas in classes:
            print(f'{clas.id}: {clas.name}')

    def displayTeachers(self):
        teachers = self.db.getTeachers()
        print("Öğretmen Listesi")
        for t in teachers:
            print(f'{t.id} - {t.name} {t.surname} / {t.branch}')

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

    def displayLessons(self):
        lessons = self.db.getLessons()
        print("Ders Listesi")
        for lesson in lessons:
            print(f'{lesson.id} - {lesson.name} | Öğretmen: {lesson.teacher_name} {lesson.teacher_surname} ({lesson.teacher_branch}) | Sınıf: {lesson.class_name}')

app = App()     
app.initApp()