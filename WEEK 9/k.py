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
