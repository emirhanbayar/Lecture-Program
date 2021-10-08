import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class Dbmanager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
        

    def getStudentById(self,id):
        sql = "SELECT * FROM students WHERE id = '%s'"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        except mysql.connector.Error as err:
            print('hata: ',err)


    def getStudentsByClassId(self,classid):
        sql = "SELECT * FROM students WHERE classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print('hata: ',err)

    
    def addStudent(self, student: Student):
        sql = "INSERT INTO students(Student_Number,Name,Surname,Birth_Date,Gender,classid) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata: ',err)

    def editStudent(self, student: Student):
        sql = "update students set Student_Number=%s,Name=%s,Surname=%s,Birth_Date=%s,Gender=%s where id=%s"
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.id)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.Error as err:
            print('hata: ',err)
    
    def deleteStudent(self, student: Student):
        sql = "DELETE FROM students WHERE id = %s"
        value = (student.id,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi')
        except mysql.connector.Error as err:
            print('Hata:',err)

        





