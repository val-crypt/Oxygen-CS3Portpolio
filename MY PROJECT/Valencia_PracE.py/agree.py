class Student:
    def __init__(self,name):
        self.name = name

class School:
    def __init__(self,name):
        self.name = name
        self.students = [] #list of students

    def add_student(self,student):                  
        self.students.append(student)

#Example usage
school1 = School("Philippine Science High School")
s1 = Student("Uno")
s2 = Student("Ej")
s3 = Student("Dwenie")
s4 = Student("Vince")
school1.add_student(s1)
school1.add_student(s2)
school1.add_student(s3)
school1.add_student(s4)

print(f"School Name: {school1.name}")
print(f"List of Students:")
for student in school1.students:
    print(f" - {student.name}") 

school2 = School("Virginia Centurione Bracelli School")
s1 = Student("Alex")
s2 = Student("Alei")
s3 = Student("Cess")
s4 = Student("Dane")

school2.add_student(s1)
school2.add_student(s2)
school2.add_student(s3)
school2.add_student(s4)

print(f"School Name: {school2.name}")
print("List of Students:")
for student in school2.students:
    print(f" - {student.name}") 
