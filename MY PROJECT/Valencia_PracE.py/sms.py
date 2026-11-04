class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
student1 = Student("Uno", 90)

class Teacher:      
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

student1 = Student("Uno", 90)
student2 = Student("EJ", 91)
student3 = Student("Placado", 75)

teacher1 = Teacher("Sir B", "Math")
teacher1.add_student(student1)
teacher1.add_student(student2)
teacher1.add_student(student3)

for student in teacher1.students:
    print(student.name)

class Course:
    def __init__(self,name):
        self.name = name
        self.students = []

math = Course("Math")
science = Course("Science")