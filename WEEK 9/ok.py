class Student:
    DEFAULT_SUBJECT = ["Electronics", "Computer Programming"]

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"{self.name} grade: {self.grade} subject: {self.subject}")

    @classmethod
    def create_default_student(cls, name, grade):
        print(f"{name} grade: {grade} subject: {cls.DEFAULT_SUBJECT}")

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.0


if __name__ == "__main__":
    student1 = Student(name="Barney", grade=5.00, subject=["Materials Engineering", "Chemistry"])
    student1.print_student_info_method()
    if Student.is_grade_passing(student1.grade):
        print("pass")
    else:
        print("fail")

    student2 = Student.create_default_student(name="Morlock", grade=1.25)
