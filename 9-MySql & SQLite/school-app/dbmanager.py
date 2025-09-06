import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Class import Class
from Teacher import Teacher
from Lesson import Lesson
from classlesson import ClassLesson

# genel olarak tüm alınan verileri listenin içinde class nesnesi olarak saklıyoruz

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id = %s"
        value  = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def deleteStudent(self, studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentsByClassId(self, classid):
        sql = "select * from student where classid = %s"
        value  = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addorEditStudent(self, student: Student):
        if not student.id or student.id == 0:
            sql = "INSERT INTO Student(studentNumber, name, surname, birthdate, gender, classId) VALUES (%s,%s,%s,%s,%s,%s)"
            value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
            self.cursor.execute(sql, value)

            try:
                self.connection.commit()
                print(f'{self.cursor.rowcount} tane kayıt eklendi.')
            except mysql.connector.Error as err:
                print('hata:', err)
        else:
            sql = "update student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s where id=%s"
            value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
            self.cursor.execute(sql, value)

            try:
                self.connection.commit()
                print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
            except mysql.connector.Error as err:
                print('hata:', err)

    def getTeachers(self):
        sql = "select * from teacher"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getTeacherById(self,id):
        sql = "select * from teacher where id = %s"
        value  = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print('Error:', err)
    
    def addorEditTeacher(self, teacher: Teacher):
        if not teacher.id or teacher.id == 0:
            sql = "INSERT INTO Teacher(branch, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
            value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)
            self.cursor.execute(sql, value)

            try:
                self.connection.commit()
                print(f'{self.cursor.rowcount} tane öğretmen eklendi.')
            except mysql.connector.Error as err:
                print('hata:', err)
        else:
            sql = "UPDATE Teacher SET branch=%s, name=%s, surname=%s, birthdate=%s, gender=%s WHERE id=%s"
            value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.id)
            self.cursor.execute(sql, value)

            try:
                self.connection.commit()
                print(f'{self.cursor.rowcount} tane öğretmen güncellendi.')
            except mysql.connector.Error as err:
                print('hata:', err)

    def getLessons(self):
        sql = """ SELECT lesson.name, class.name, teacher.name, teacher.surname FROM lesson,class_lesson, class, teacher WHERE lesson.id = class_lesson.lessonid AND class_lesson.classid = class.id AND class_lesson.teacherid = teacher.id; """
        self.cursor.execute(sql)
        try:
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print('Error:', err)

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print('db silindi')