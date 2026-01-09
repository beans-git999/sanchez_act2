student1_name = "Miguel"
student1_grade = "1.0"
student1_subject = ["Calculus", "Physics"]

student2_name = "Michael"
student2_grade = "1.25"
student2_subject = ["UTS", "Elex"]

student3_name = "Morlock"
student3_grade = "2.00"
student3_subject = ["Economics", "Chemistry"]

def print_student_info(name, grade, subject):
    print(f"{name} grade: {grade} course: {subject}")

if __name__ == "__main__":
#print_student_info(student1_name, student1_grade, student1_subject)
#print_student_info(student2_name, student2_grade, student2_subject)
#print_student_info(student3_name, student3_grade, student3_subject)

class Student:

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def print_student_info(self):
        print(f"{self.name} grade: {self.grade} course: {self.subject}")

if __name__ == "__main__":
    student1 = Student("Bogart", "1.25", ["Economics", "Chemistry"])
    student1.print_student_info()
    student2 = Student("Kevin", "1.00", ["Economics", "Chemistry"])
    student2.print_student_info()
    student3 = Student("Roldan", "1.25", ["Economics", "Chemistry"])
    student3.print_student_info()





