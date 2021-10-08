from dbmanager import Dbmanager
import datetime
from Student import Student

class App():
    def __init__(self):
        self.db = Dbmanager()
    
    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış (E/H)\n"
        while True:
            print(msg)
            islem = input("Seçiminiz: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
            elif islem == 'Ç' or islem == 'E':
                pass
    
    def displayClasses(self):
        classes = self.db.getClasses()
        for sinif in classes:
            print(f'{sinif.id}: {sinif.name}')
        
    def displayStudents(self):
        self.displayClasses()

        classid = input("Hangi sınıf: ")

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        for student in students:
            print(f'{student.id}-{student.name} {student.surname}')
        return classid

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf: "))
        number = int(input("numara: "))
        name = input("ad: ")
        surname = input("soyad: ")
        year = int(input("yıl: "))
        month = int(input("ay: "))
        day = int(input("gün: "))
        birthdate = datetime.date(year=year, month=month, day=day)
        gender = input("Cinsiyet (E/K): ")

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
    
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id: "))
        student = self.db.getStudentById(studentid)
        student.studentNumber = input("Öğrenci numarası: ") or student.studentNumber
        student.name = input("Ad: ") or student.name
        student.surname = input("Soyad: ") or student.surname
        student.gender = input("Cinsiyet: ") or student.gender
        student.classid = input("Sınıf: ") or student.classid
        year = input("Doğum yılı: ") or student.birthdate.year
        month = input("Doğum ayı: ") or student.birthdate.month
        day = input("Doğum günü: ") or student.birthdate.day
        student.birthdate = datetime.date(year=year, month=month, day=day)

        self.db.editStudent(student)

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id: "))
        student = self.db.getStudentById(studentid)

        self.db.deleteStudent(student)
        






app = App()
app.initApp()
