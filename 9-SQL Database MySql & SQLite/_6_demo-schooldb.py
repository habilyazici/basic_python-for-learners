import mysql.connector
from datetime import datetime

class Student:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="ogrenci")
    mycursor = connection.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender):
        if id is not None:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO ogrenci(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO ogrenci(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)
        Student.connection.commit()
        print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')

    @staticmethod
    def getStudentById(id):
        sql = "select * from ogrenci where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        except mysql.connector.Error as err:
            print('Error', err)        
    
    def updateStudent(self):
        sql = "update ogrenci set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)
        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    @staticmethod
    def updateStudents(studentList):
        sql = "update ogrenci set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []

        order = (1, 2, 3, 4, 5, 0)  
        # Yapmak istediğimiz sıralama: studentNumber, name, surname, birthdate, gender, id
        for student in studentList:
            # Her öğrenci kaydını, 'order' sırasına göre yeniden diziyoruz
            new_student = []
            for i in order:
                new_student.append(student[i])
            values.append(new_student)

        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from ogrenci where gender = %s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)
            return None

    def __del__(self):
        Student.mycursor.close()
        Student.connection.close()

# student1 = Student('2023002', 'Mehmet', 'Kars', datetime(2003, 12, 9), 'E')
# student1.saveStudent()
# print("\n" + 20 * '-' + "\n")


# students= [
#     (2023016, 'Selim', 'Erkan', datetime(2003, 12, 9), 'E'),
#     (2023003, 'Ayşe', 'Uçar', datetime(2005, 5, 15), 'K'),
#     (2023004, 'Ali', 'Alim', datetime(2004, 8, 22), 'E'),
# ]
# Student.saveStudents(students)
# print("\n" + 20 * '-' + "\n")


# student = Student.getStudentById(8)
# student.name = 'Çınar'
# student.updateStudent()
# print("\n" + 20 * '-' + "\n")


students = Student.getStudentsGender('E')
print(students)

# studentList = []
# for student in students:
#     student = list(student)
#     student[2] = 'Mr ' + student[2]
#     # veriler liste kaldı ama executemany() liste içinde liste de gönderir.
#     studentList.append(student)
# print(studentList)
# Student.updateStudents(studentList)
# print("\n" + 20 * '-' + "\n")


# mr 'ları kaldırma
# studentList = []
# for student in students:
#     student = list(student)
#     if student[2].startswith('Mr '):
#         student[2] = student[2][3:]  # "Mr " kaldırılır
#     studentList.append(student)
# print(studentList)
# Student.updateStudents(studentList)